import sys
from VMParser import VMParser
from VMCodeWriter import VMCodeWriter
class VMTranslator:
    def __init__(self):
        self.parser = None
        self.codewriter = None
        self.counter = 0
    def translate(self, vm_file):
        asm_file = vm_file.replace('.vm', '.asm')

        self.parser = VMParser(vm_file)
        self.codewriter = VMCodeWriter(asm_file)

        while self.parser.has_more_commands():
            self.parser.advance()
            cmd_type = self.parser.cmd_type()

            if cmd_type in ['C_PUSH', 'C_POP']:
                segment = self.parser.arg1()
                index = self.parser.arg2()
                print('segment:' + str(segment))
                print('index:' + str(index))
                self.codewriter.write_push_pop(cmd_type, segment, index)
            elif cmd_type == 'C_ARITHMETIC':
                command = self.parser.arg1()
                self.codewriter.write_arithmetic(command)
            elif cmd_type == 'C_LABEL':
                label = self.parser.arg1()
                self.codewriter.write_label(label)
            elif cmd_type == 'C_GOTO':
                label = self.parser.arg1()
                self.codewriter.write_goto(label)
            elif cmd_type == 'C_IF':
                label = self.parser.arg1()
                self.codewriter.write_if(label)
            elif cmd_type == 'C_FUNCTION':
                function_name = self.parser.arg1()
                n_vars = self.parser.arg2()
                self.codewriter.write_function(function_name, n_vars)
            elif cmd_type == 'C_CALL':
                function_name = self.parser.arg1()
                n_args  = self.parser.arg2()
                self.codewriter.write_call(function_name, n_args)
            elif cmd_type == 'C_RETURN':
                self.codewriter.write_return()
            
            print(cmd_type)
            self._test_count()
            
        self.parser.close()
        self.codewriter.close()
        return True
    
    def _test_count(self):
        self.counter += 1
        print(f'执行了{self.counter}次')

def main():
    vm_file = sys.argv[1]
    translator = VMTranslator()
    success = translator.translate(vm_file)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()