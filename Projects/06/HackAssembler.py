"先实现一个不处理符号的汇编编译器"

from Code import Code 
from Parser import Parser

class NoSymbolAssembler:
    def __init__(self):
        self.Parser = None
        self.Code = Code()

    def assemble(self, input_stream, output_file):
        "实现汇编操作"
        machine_codes = self._parse_and_translate(input_stream)
        self._write_output(output_file, machine_codes)


    def _parse_and_translate(self, input_stream):
        "解析输入指令并翻译为机器码"
        machine_codes = []
        self.Parser = Parser(input_stream)

        while self.Parser.has_more_lines:
            self.Parser.advance()
            machine_code = self.translate_current_instruction()
            machine_codes.append(machine_code)

        return machine_codes

    def _translate_current_instruction(self):
        "将指令翻译成机器码"
        cmd_type = self.Parser.instruction_type()  #判断指令类型
        
        if cmd_type == "A_INSTRUCTION":
            symbol = self.Parser.symbol()
            address = int(symbol)
            return f'0{address:015b}'
        
        if cmd_type == "C_INSTRUCTION":
            dest = self.Parser.dest()
            comp = self.Parser.comp()
            jump = self.Parser.jump()
            return f'111{dest}{comp}{jump}'

    def _write_output(self, output_file, machine_codes):
        "输出机器码文件"
        with open(output_file, 'w') as f:
            for code in machine_codes:
                f.write(code + '\n')