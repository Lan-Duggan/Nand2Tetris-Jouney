class VMParser:
    def __init__(self, vm_file):
        self.vm_file = open(vm_file, 'r')
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
                self.current_command = clean_line
                return True
    
    def advance(self):
        return self.current_command
    
    def cmd_type(self):
        if self.current_command.startswith('push'):
            return 'C_PUSH'
        elif self.current_command.startswith('pop'):
            return 'C_POP'
        else:
            return 'C_ARITHMETIC'
    
    def arg1(self):
        if self.cmd_type == 'C_ARITHMETIC':
            return self.current_command
        elif self.cmd_type in ['C_PUSH', 'C_POP']:
            return self.current_command.split()[1]
        
    def arg2(self):
        if self.cmd_type in ['C_PUSH', 'C_POP']:
            return int(self.current_command.split()[2])
        
    def close(self):
        self.vm_file.close()