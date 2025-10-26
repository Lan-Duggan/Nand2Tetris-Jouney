class VMParser:
    def __init__(self, vm_file):
        self.vm_file = open(vm_file, 'r')
        self.current_line = None
        self.current_command= None
        self.eof = False

    def has_more_commands(self):
        """检查是否还有更多命令"""
        while True:
            line = self.vm_file.readline()
            if not line:
                self.eof = True
                return False
            
            # 清理行：移除注释和空白
            clean_line = line.split('//')[0].strip()
            if clean_line:
                self.current_line = clean_line
                return True
    
    def advance(self):
        self.current_command = self.current_line
    
    def cmd_type(self):
        cmd_map = {
            'push' : 'C_PUSH',
            'pop' : 'C_POP',
            'label': 'C_LABEL',
            'goto': 'C_C_GOTO',
            'if-goto': 'C_IF',
            'function': 'C_FUNCTION',
            'call': 'C_CALL',
            'return': 'C_RETURN',
        }
        
        arithmetic_commands = [
        'add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'
        ]
        
        cmd = self.current_command.split()[0]

        if cmd in cmd_map:
            return cmd_map[cmd]
        elif cmd in arithmetic_commands:
            return 'C_ARITHMETIC'
    
    def arg1(self):
        cmd_type = self.cmd_type()
        if cmd_type == 'C_ARITHMETIC':
            return self.current_command
        elif cmd_type in ['C_LABEL', 'C_GOTO', 'C_IF']:
            return self.current_command.split()[1]
        elif cmd_type in ['C_FUNCTION', 'C_CALL', 'C_RETURN']:
            return self.current_command.split()[1]
        elif cmd_type in ['C_PUSH', 'C_POP']:
            return self.current_command.split()[1]
        
    def arg2(self):
        cmd_type = self.cmd_type()
        if cmd_type in ['C_PUSH', 'C_POP']:
            return int(self.current_command.split()[2])
        elif cmd_type in ['C_FUNCTION', 'C_CALL', 'C_RETURN']:
            return int(self.current_command.split()[2])
        
    def close(self):
        self.vm_file.close()