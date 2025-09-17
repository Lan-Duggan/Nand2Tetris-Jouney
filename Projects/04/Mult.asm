@R2
M = 0

(LOOP)
@R1
D = M

@END
D;JEQ

@R2
D = M

@R5
D = D + M

@R1
D = D - 1

@LOOP
0;JMP

@END
0,JMP