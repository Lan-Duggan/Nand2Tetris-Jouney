SimpleFunction.test
@0
D = A
@SP
A = M
M = D
SP
M = M + 1
@0
D = A
@SP
A = M
M = D
SP
M = M + 1
@0
D = A
@LCL
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
@1
D = A
@LCL
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M = M - 1
A = M
D = M
@SP
M  = M - 1
A = M
A + M
@SP
M = M + 1
@SP
M = M -1
A = M
M = !M
@0
D = A
@ARG
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M = M - 1
A = M
D = M
@SP
M  = M - 1
A = M
A + M
@SP
M = M + 1
@1
D = A
@ARG
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M = M - 1
A = M
D = M
@SP
M  = M - 1
A = M
A - M
@SP
M = M + 1
@LCL
D = M
@5
A = D - A
D = M
@R13
M = D
@SP
A = M-1
D = M
@ARG
A = M
M = D
@ARG
D = M+1
@SP
M = D
@LCL
D = M
@1
A = D - A
D = M
@TAHT
M = D
@LCL
D = M
@2
A = D - A
D = M
@THIS
M = D
@LCL
D = M
@3
A = D - A
D = M
@ARG
M = D
@LCL
D = M
@4
A = D - A
D = M
@LCL
M = D
@R13
A = M
0;JMP
