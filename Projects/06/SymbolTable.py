"实现符号表"

class SymbolTable:
    def __init__(self):
        self._symbol_dict = {
            # 预定义符号
            'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
            # 寄存器 R0-R15
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4,
            'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9,
            'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
            # I/O 映射
            'SCREEN': 16384, 'KBD': 24576
        }

    def add_entry(self, symbol, address):
        "添加新的映射关系"
        self._symbol_dict[symbol] = address

    def contains(self, symbol):
        "查询symbol是否在表中"
        return symbol in self._symbol_dict
    
    def get_address(self, symbol):
        "返回与symbol相关联的地址"
        return self._symbol_dict[symbol]
