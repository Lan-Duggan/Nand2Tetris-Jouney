class VMCodeWriter:
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')
        self.label_counter = 0

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

    def close(self):
        self.output_file.close()