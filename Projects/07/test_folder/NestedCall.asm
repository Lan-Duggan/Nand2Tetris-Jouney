Sys.init
@4000
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M=M-1
A=M
D=M
@THIS
M=D
@5000
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
@RETURN_0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = A
@SP
A = M
M = D
@SP
M = M +1
@ARG
D = A
@SP
A = M
M = D
@SP
M = M +1
@THIS
D = A
@SP
A = M
M = D
@SP
M = M +1
@THAT
D = A
@SP
A = M
M = D
@SP
M = M +1
@SP
D = M
@5
D = D - A
f@{n_args}
D = D - A
@ARG
M = D
@SP
D = A
@LCL
M = D
@Sys.main
0;JMP
(RETURN_0)
@SP
M=M-1
A=M
D=M
@6
M=D
(Sys.init$LOOP)
Sys.main
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
@SP
A = M
M = D
SP
M = M + 1
@4001
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M=M-1
A=M
D=M
@THIS
M=D
@5001
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
@200
D = M
@SP
A = M
M = D
@SP
M = M + 1
@1
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@40
D = M
@SP
A = M
M = D
@SP
M = M + 1
@2
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@6
D = M
@SP
A = M
M = D
@SP
M = M + 1
@3
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@123
D = M
@SP
A = M
M = D
@SP
M = M + 1
@RETURN_1
D = A
@SP
A = M
M = D
@SP
M = M + 1
@LCL
D = A
@SP
A = M
M = D
@SP
M = M +1
@ARG
D = A
@SP
A = M
M = D
@SP
M = M +1
@THIS
D = A
@SP
A = M
M = D
@SP
M = M +1
@THAT
D = A
@SP
A = M
M = D
@SP
M = M +1
@SP
D = M
@5
D = D - A
f@{n_args}
D = D - A
@ARG
M = D
@SP
D = A
@LCL
M = D
@Sys.add12
0;JMP
(RETURN_1)
@SP
M=M-1
A=M
D=M
@5
M=D
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
@2
D = A
@LCL
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
@3
D = A
@LCL
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
@4
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
M = M - 1
A = M
D = M
@SP
M  = M - 1
A = M
A + M
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
Sys.add12
@4002
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M=M-1
A=M
D=M
@THIS
M=D
@5002
D = M
@SP
A = M
M = D
@SP
M = M + 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
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
@12
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
