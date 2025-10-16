class Code:
    "将符号字段翻译成二进制"
    DEST_TABLE = {
        None:"000",
        "M":"001",
        "D":"010",
        "DN":"011",
        "A":"100",
        "AM":"101",
        "AD":"110",
        "ADM":"111",
    }

    COMP_TABLE = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000", "M": "1110000",
        "!D": "0001101",
        "!A": "0110001", "!M": "1110001",
        "-D": "0001111",
        "-A": "0110011", "-M": "1110011",
        "D+1": "0011111",
        "A+1": "0110111", "M+1": "1110111",
        "D-1": "0001110",
        "A-1": "0110010", "M-1": "1110010",
        "D+A": "0000010", "D+M": "1000010",
        "D-A": "0010011", "D-M": "1010011",
        "A-D": "0000111", "M-D": "1000111",
        "D&A": "0000000", "D&M": "1000000",
        "D|A": "0010101", "D|M": "1010101"
    }
    
  
    JUMP_TABLE = {
        None: "000",  
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }


    @staticmethod
    def dest(mnemonic):
        return Code.DEST_TABLE.get(mnemonic, '000')


    @staticmethod
    def comp(mnemonic):
        return Code.COMP_TABLE[mnemonic]


    @staticmethod
    def jump(mnemonic):
        return Code.JUMP_TABLE.get(mnemonic, '000')


# 使用示例
def test_code_module():
    # 测试dest方法
    print("Dest测试:")
    print(f"M -> {Code.dest('M')}")      # 输出: 001
    print(f"D -> {Code.dest('D')}")      # 输出: 010
    print(f"A -> {Code.dest('A')}")      # 输出: 100
    print(f"空 -> {Code.dest('')}")      # 输出: 000
    
    # 测试comp方法
    print("\nComp测试:")
    print(f"0 -> {Code.comp('0')}")     # 输出: 0101010
    print(f"D -> {Code.comp('D')}")      # 输出: 0001100
    print(f"A -> {Code.comp('A')}")      # 输出: 0110000
    print(f"M -> {Code.comp('M')}")      # 输出: 1110000
    print(f"D+M -> {Code.comp('D+M')}")  # 输出: 1000010
    
    # 测试jump方法
    print("\nJump测试:")
    print(f"JGT -> {Code.jump('JGT')}")  # 输出: 001
    print(f"JEQ -> {Code.jump('JEQ')}")  # 输出: 010
    print(f"JMP -> {Code.jump('JMP')}")  # 输出: 111
    print(f"空 -> {Code.jump('')}")      # 输出: 000

if __name__ == "__main__":
    test_code_module()