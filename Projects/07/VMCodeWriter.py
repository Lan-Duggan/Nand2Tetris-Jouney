class VNCodeWriter:
    def __init__(self, output_file):
        self.output_file = open(output_file, 'w')
        self.label_counter = 0


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
