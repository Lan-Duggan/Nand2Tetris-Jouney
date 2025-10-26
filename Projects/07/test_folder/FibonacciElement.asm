Main.fibonacci
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
@2
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
@Main.fibonacci$N_LT_2
D;JNE
(Main.fibonacci$N_LT_2)
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
(Main.fibonacci$N_GE_2)
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
@2
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
@Main.fibonacci
0;JMP
(RETURN_0)
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
@1
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
@Main.fibonacci
0;JMP
(RETURN_1)
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
Sys.init
@4
D = M
@SP
A = M
M = D
@SP
M = M + 1
@RETURN_2
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
@Main.fibonacci
0;JMP
(RETURN_2)
(Sys.init$END)
