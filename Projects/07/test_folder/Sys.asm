Sys.init
@6
D = M
@SP
A = M
M = D
@SP
M = M + 1
@8
D = M
@SP
A = M
M = D
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
@Class1.set
0;JMP
(RETURN_0)
@SP
M=M-1
A=M
D=M
@5
M=D
@23
D = M
@SP
A = M
M = D
@SP
M = M + 1
@15
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
@Class2.set
0;JMP
(RETURN_1)
@SP
M=M-1
A=M
D=M
@5
M=D
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
@Class1.get
0;JMP
(RETURN_2)
@RETURN_3
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
@Class2.get
0;JMP
(RETURN_3)
(Sys.init$END)
