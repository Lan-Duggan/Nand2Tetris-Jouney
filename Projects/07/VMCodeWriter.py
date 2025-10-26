class VMCodeWriter:
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')
        self.label_counter = 0
        self.return_counter = 0
        self.current_function = ''

    def set_file_name(self, file_name):
        "设置当前文件名（用于静态变量）"
        self.current_file = file_name

    def write_arithmetic(self, command):
        asm_code = []

        # 一元运算符操作
        if command in ['neg', 'not']:
            asm_code.extend([
                '@SP',
                'M = M -1',
                'A = M'
            ]
            )

            if command == 'neg':
                asm_code.append('M = -M')
            elif command == 'not':
                asm_code.append('M = !M')
        
        # 二元运算符操作
        elif command in ['add', 'sub', 'and', 'or']:
            asm_code.extend([
                '@SP',
                'M = M - 1',
                'A = M', #A 是 M 的索引，修改索引位置
                'D = M', #第二个元素y

                '@SP',
                'M  = M - 1', #第一个元素x
                'A = M',
            ])

            if command == 'add':
                asm_code.append('A + M')
            elif command == 'sub':
                asm_code.append('A - M')
            elif command == 'and':
                asm_code.append('A & M')
            elif command == 'or':
                asm_code.append('A | M')

            asm_code.extend([
                '@SP',
                'M = M + 1',
            ])
        
        # 比较操作
        elif asm_code in ['eq', 'gt', 'lt']:
            label_true = f"TRUE.{self.label_counter}"
            label_end = f"END.{self.label_counter}"
            asm_code.extend([
                '@SP',
                'M = M - 1',
                'A = M',
                'D = M',

                '@SP',
                'M = M - 1',
                'A = M',
                'D = M - D',
                f'@{label_true}',
            ])

            if asm_code == 'eq':
                asm_code.append('D;JEQ')
            elif asm_code == 'gt':
                asm_code.append('D;JGT')
            elif asm_code == 'lt':
                asm_code.append('D;JLT')

            asm_code.extend([
                '@SP',
                'A = M',
                'M = 0',
                f'@{label_end}',
                '0;JMP',
                
                f'{label_true}',
                '@SP',
                'M = -1',

                f'{label_end}',
                '@SP',
                'M = M + 1',
            ])

        for line in asm_code:
            self.output_file.write(line + '\n')

    def write_push_pop(self, command, segment, index):
        if command == 'C_PUSH':
            self._write_push(segment, index)
        elif command == 'C_POP':
            self._write_pop(segment, index)

    def _write_push(self, segment, index):
        asm_code = []

        # 获取要压栈的值存入D寄存器
        if segment in ['local', 'argument', 'this', 'that']:
            segment_map = {'local':'LCL', 'argument':'ARG', 'this':'THIS', 'that':'THAT'}
            seg_sybmol = segment_map[segment]
            asm_code.extend([
                f'@{index}',
                'D = A',
                f'@{seg_sybmol}',
                'A = D + M',
                'D = M', # D = RAM(base + i)
            ])
        elif segment == 'pointer':
            seg_sybmol = 'THIS' if index == 0 else 'THAT'
            asm_code.extend([
                f'@{seg_sybmol}',
                'D = M',
            ])
        elif segment == 'temp':
            asm_code.extend([
                f'@{5 + index}',
                'D = M'
            ])
        elif segment == 'constant':
            asm_code.extend([
                f'@{index}',
                'D = M'
            ])
        elif segment == 'static':
            asm_code.extend([
                f'@{self.current_file}{index}',
                'D = M'
            ])
        
        # 压栈操作
        asm_code.extend([
            '@SP',
            'A = M',
            'M = D',
            '@SP',
            'M = M + 1'
        ])


        for line in asm_code:
            self.output_file.write(line + '\n')

    def _write_pop(self, segment, index):
        asm_code = []
        
        if segment == 'constant':
            raise ValueError("不能pop到constant段")
        
        elif segment in ['local', 'argument', 'this', 'that']:
            seg_map = {'local': 'LCL', 'argument': 'ARG', 'this': 'THIS', 'that': 'THAT'}
            seg_symbol = seg_map[segment]
            
            asm_code.extend([
                f'@{index}',
                'D=A',
                f'@{seg_symbol}',
                'D=D+M',
                '@R13',  # 使用R13存储目标地址
                'M=D',
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@R13',
                'A=M',
                'M=D'
            ])
        
        elif segment == 'static':
            asm_code.extend([
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                f'@{self.current_file}.{index}',
                'M=D'
            ])
        
        elif segment == 'temp':
            asm_code.extend([
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                f'@{5 + index}',
                'M=D'
            ])
        
        elif segment == 'pointer':
            seg_symbol = 'THIS' if index == 0 else 'THAT'
            asm_code.extend([
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                f'@{seg_symbol}',
                'M=D'
            ])
        
        for line in asm_code:
            self.output_file.write(line + '\n')       
            
    def _write_lines(self, lines):
        for line in lines:
            self.output_file.write(line + '\n')

    def write_label(self, label):
        full_label = f'{self.current_function}${label}' if self.current_function else label
        self._write_lines([f'({full_label})'])

    def write_goto(self, label):
        full_label = f'{self.current_function}${full_label}' if self.current_function else label
        self._write_lines([
            f'@{full_label}',
            '0;JMP'
        ])
    
    def write_if(self, label):
        full_label = f'{self.current_function}${label}' if self.current_function else label
        self._write_lines([
            '@SP',
            'M = M - 1',
            'A = M',
            'D = M',
            f'@{full_label}',
            'D;JNE'
        ])

    def write_call(self, function_name, n_args):
        return_label = f'RETURN_{self.return_counter}'
        self.return_counter += 1

        # 保存返回地址
        self._write_lines([
            f'@{return_label}',
            'D = A',
            '@SP',
            'A = M',
            'M = D',
            '@SP',
            'M = M + 1'
        ])

        # 保存原指针状态
        for segment in ['LCL', 'ARG', 'THIS', 'THAT']:
            self._write_lines([
                f'@{segment}',
                'D = A',
                '@SP',
                'A = M',
                'M = D',
                '@SP',
                'M = M +1'
            ])
        
        # 修改现指针状态
        # 设置新ARG指针
        self._write_lines([
            '@SP',
            'D = M',
            '@5',
            'D = D - A',
            'f@{n_args}',
            'D = D - A',
            '@ARG',
            'M = D'
        ])

        #设置新LCL指针
        self._write_lines([
            '@SP',
            'D = A',
            '@LCL',
            'M = D'
        ])

        # 跳转到函数
        self._write_lines([
            f'@{function_name}',
            '0;JMP',
            f'({return_label})'
        ])


    def write_function(self, function_name, n_vars):
        self.current_function = function_name
        self._write_lines([f'{function_name}'])
        
        for i in range(n_vars):
            self._write_lines([
                '@0',
                'D = A',
                '@SP',
                'A = M',
                'M = D',
                'SP',
                'M = M + 1'
            ])

    def write_return(self):
        # 保存返回地址到临时变量
        self._write_lines([
            '@LCL',
            'D = M', # Not D = A, @LCL是获取指向LCL寄存器的地址， LCL寄存器存储着local内存单元的起始位置
            '@5',
            'A = D - A',
            'D = M',
            '@R13',
            'M = D'
        ])
        
        # 将返回值保存到ARG[0]
        self._write_lines([
            '@SP',
            'A = M-1',
            'D = M',
            '@ARG',
            'A = M',
            'M = D'
        ])

        # 恢复指针SP
        self._write_lines([
            '@ARG',
            'D = M+1',
            '@SP',
            'M = D'
        ])
        
        # 恢复其他指针
        segments = ['TAHT', 'THIS', 'ARG', 'LCL']
        for i , segment in enumerate(segments):
            offset = i + 1
            self._write_lines([
                '@LCL',
                'D = M',
                f'@{offset}',
                'A = D - A',
                'D = M',
                f'@{segment}',
                'M = D'
            ])
        
        # 跳转到返回地址
        self._write_lines([
            '@R13',
            'A = M',
            '0;JMP'
        ])



    def close(self):
        self.output_file.close()
        



