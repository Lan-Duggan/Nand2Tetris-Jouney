// =============================================
// 函数: Math.factorial
// 功能: 计算n的阶乘 (n!)
// 参数: n (argument 0)
// 局部变量: 1个（用于临时存储）
// 调用约定: 递归实现
// =============================================

// function Math.factorial 1
(Math.factorial)
// 初始化局部变量为0
@0

@SP
A=M
M=D
@SP
M=M+1

// =============================================
// 递归基检查: if n == 1
// =============================================

// push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq (n == 1 ?)
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE_0
D;JEQ

// false分支 (n != 1)
@SP
A=M
M=0
@END_EQ_0
0;JMP

// true分支 (n == 1)
(TRUE_0)
@SP
A=M
M=-1

(END_EQ_0)
@SP
M=M+1

// if-goto BASE_CASE
@SP
M=M-1
A=M
D=M
@BASE_CASE
D;JNE

// =============================================
// 递归调用: factorial(n-1)
// =============================================

// push argument 0 (n)
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub (n - 1)
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1

// call Math.factorial 1
// 保存返回地址
@RETURN_ADDRESS_0
D=A
@SP
A=M
M=D
@SP
M=M+1

// 保存调用者状态
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// 设置新ARG (SP - 5 - n_args)
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D

// 设置新LCL
@SP
D=M
@LCL
M=D

// 跳转到函数
@Math.factorial
0;JMP

// 返回地址标签
(RETURN_ADDRESS_0)

// =============================================
// 计算 n * factorial(n-1)
// =============================================

// push argument 0 (n)
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1

// mult (n * factorial(n-1))
// 注意：Hack汇编需要实现乘法，这里假设有mult函数
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M*D
@SP
M=M+1

// return
@LCL
D=M
@5
A=D-A
D=M
@R13
M=D

@SP
A=M-1
D=M
@ARG
A=M
M=D

@ARG
D=M+1
@SP
M=D

@LCL
D=M
@1
A=D-A
D=M
@THAT
M=D

@LCL
D=M
@2
A=D-A
D=M
@THIS
M=D

@LCL
D=M
@3
A=D-A
D=M
@ARG
M=D

@LCL
D=M
@4
A=D-A
D=M
@LCL
M=D

@R13
A=M
0;JMP

// =============================================
// 递归基: n == 1 时返回1
// =============================================

(BASE_CASE)
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// return
@LCL
D=M
@5
A=D-A
D=M
@R13
M=D

@SP
A=M-1
D=M
@ARG
A=M
M=D

@ARG
D=M+1
@SP
M=D

@LCL
D=M
@1
A=D-A
D=M
@THAT
M=D

@LCL
D=M
@2
A=D-A
D=M
@THIS
M=D

@LCL
D=M
@3
A=D-A
D=M
@ARG
M=D

@LCL
D=M
@4
A=D-A
D=M
@LCL
M=D

@R13
A=M
0;JMP