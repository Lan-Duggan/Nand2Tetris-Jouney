"完整汇编器的实现"

import sys
from CodeModule import Code 
from ParserModule import Parser
from SymbolTable import SymbolTable

class HackAssembler:
    def __init__(self):
        self.parser = None
        self.code = Code()
        self.symbol_table = SymbolTable() #创建符号表
        self.next_variable_address = 16


    def assemble(self, input_file, output_file):
        self._first_pass(input_file)
        machine_codes = self._second_pass(input_file)
        self._write_output(output_file, machine_codes)

    def _first_pass(self, input_file):
        self.parser = Parser(input_file)
        rom_address = 0 

        while self.parser.have_more_lines():
            self.parser.advance()
            cmd_type = self.parser.instruction_type()
            if cmd_type == "L_INSTRUCTION":
                symbol = self.parser.symbol()
                self.symbol_table.add_entry(symbol, rom_address)
            elif cmd_type in ["A_INSTRUCTION", "C_INSTRUCTION"]:
                rom_address += 1

        self.parser.close()

    def _second_pass(self, input_file):
        self.parser = Parser(input_file)
        machine_codes = []

        while self.parser.have_more_lines():
            self.parser.advance()
            cmd_type  =self.parser.instruction_type()

            if cmd_type == "A_INSTRUCTION":
                machine_code = self._translate_a_instruction()
                machine_codes.append(machine_code)
            elif cmd_type == "C_INSTRUCTION":
                machine_code = self._translate_c_instruction()
                machine_codes.append(machine_code)
        self.parser.close()
        return machine_codes       
            
    def _translate_a_instruction(self):
        """翻译A指令为机器码"""
        symbol = self.parser.symbol()
        
        if symbol.isdigit():
            # 若@数字
            address = int(symbol)
        else:
            # 若@符号
            if not self.symbol_table.contains(symbol):
                self.symbol_table.add_entry(symbol, self.next_variable_address)
                self.next_variable_address+= 1
            address = self.symbol_table.get_address(symbol)
        
        return f"0{address:015b}"  

    def _translate_c_instruction(self):
        """翻译C指令为机器码"""
        # 获取指令各部分
        dest = self.parser.dest()
        comp = self.parser.comp()
        jump = self.parser.jump()
        
        # 转换为二进制
        dest_bin = self.code.dest(dest)
        comp_bin = self.code.comp(comp)
        jump_bin = self.code.jump(jump)
        
        return f"111{comp_bin}{dest_bin}{jump_bin}"


    def _write_output(self, output_file, machine_codes):
        """将机器码写入输出文件"""
        with open(output_file, 'w') as f:
            for code in machine_codes:
                f.write(code + '\n')


    def run(self,input_file):
        output_file = input_file.replace('.asm', '.hack')
        self.assemble(input_file, output_file)
        return 
    


def main():
    """主函数：命令行接口"""
    input_file = sys.argv[1]
    assembler = HackAssembler()
    success = assembler.run(input_file)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()