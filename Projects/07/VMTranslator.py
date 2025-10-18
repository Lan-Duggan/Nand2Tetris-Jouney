import sys
from VMParser import VMParser
from VMCodeWriter import VMCodeWriter
class VMTranslator:
    def translate(self, vm_file):
        asm_file = vm_file.replace('.vm', '.asm')

        parser = VMParser(vm_file)
        codewriter = VMCodeWriter(asm_file)

        while parser.has_more_commands():
            parser.advance()
            cmd_type = parser.cmd_type()

            if cmd_type in ['C_PUSH', 'C_POP']:
                segment = parser.arg1()
                index = parser.arg2()
                codewriter.write_push_pop(cmd_type, segment, index)
            elif cmd_type == 'C_ARITHMETIC':
                command = parser.arg1()
                codewriter.write_arithmetic(command)

        parser.close()
        codewriter.close()
        return True

def main():
    vm_file = sys.argv[1]
    translator = VMTranslator()
    success = translator.translate(vm_file)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()