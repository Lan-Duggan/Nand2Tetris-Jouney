"The Parser Of No Symbol Assembler"

class Parser:
    def __init__(self, input_stream):
        if isinstance(input_stream, str):
            self.file = open(input_stream, "r")
            self.shouldclose = True
        else:
            self.file = input_stream
            self.shouldclose = False
        
        self.eof = False
        self.current_line = None
        self.current_command = None
    
    def have_more_lines(self):
        "判断文件当前行是否还有内容"
        while True:
            line  = self.file.readline()
            if not line:
                self.eof = True
                return False
            
            clean_line = line.split('//')[0].strip()  #清理注释和空白

            if clean_line:
                self.current_line = clean_line
                return True

    def advance(self):
        "将当前行的指令"
        self.current_command = self.current_line #将当前行的内容保存到当前指令中

    def instruction_type(self):
        "判断当前命令的类型"
        if self.current_command.startswith('@'):
            return 'A_INSTRUCTION'
        elif self.current_command.startswith('(') and self.current_command.endswith(')'):
            return 'L_INSTRUCTION'
        else:
            return 'C_INSTRUCTION'
        
    def symbol(self):
        "返回 A命令 的十进制 或 L命令的 符号 "
        instruciton_type = self.instruction_type()
        if instruciton_type == 'A_INSTRUCTION':
            return self.current_command[1:]
        if  instruciton_type == "L_INSTRUCTION":
            return self.current_command[1:-1]
        
    def dest(self):
        "提取C指令中 dest 字段部分"
        if '=' in self.current_command:
            return self.current_command.split('=')[0].strip()
        else:
            return ''
        
    def comp(self):
        "提取C指令中 comp 字段部分"
        if '=' in self.current_command:
            tempt = self.current_command.split('=')[1]
        else:
            tempt =self.current_command
        
        if ';'in tempt:
            return tempt.split(';')[0].strip()
        return tempt.strip()

    def jump(self):
        "提取C指令中 jump 字段部分"
        if ';' in self.current_command:
            return self.current_command.split(';')[1].strip()
        return ''           
    
    def close(self):
        if self.shouldclose:
            self.file.close()



# 使用Parser解析汇编代码
def parse_assembly_file(filename):
    parser = Parser(filename)
    
    try:
        while parser.has_more_lines():
            parser.advance()
            cmd_type = parser.instruction_type()
            
            print(f"INSTRUCTION: {parser.current_command}")
            print(f"Type: {cmd_type}")
            
            if cmd_type in ['A_INSTRUCTION', 'L_INSTRUCIOTN']:
                symbol = parser.symbol()
                print(f"Symbol: {symbol}")
            elif cmd_type == 'C_INSTRUCTION':
                dest = parser.dest()
                comp = parser.comp()
                jump = parser.jump()
                print(f"Dest: {dest}, Comp: {comp}, Jump: {jump}")
            
            print("---")
    finally:
        parser.close()

# 测试
if __name__ == "__main__":
    parse_assembly_file("test.asm")