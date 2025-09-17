// KED SCREEN 

(MAIN_LOOP)
// 读取键盘命令
@KED
D = M

// 判断键盘是否有输入
@CLEAR
D;JEQ

// 若有输入，开始填充屏幕
(FILL_LOOP)

@SCREEN
D = M
@address // address 存储的是当前指向屏幕的地址
M = D

@KED
D = D - A
@MAIN_LOOP
D;JEQ

@address // 先将地址指向 address
A = M    // 在读取address中存储当前屏幕的地址
M = -1

// address += 1
@address
M = M + 1

@FILL_LOOP
0;JMP

(CLEAR)

@SCREEN
D = M

@address
M = D

@KED
D = D - A

@MAIN_LOOP
D;JEQ

(CLEAR_LOOP)

@address
A = M
M = 0

@address
M = M + 1

@CLEAR_LOOP
0;JMP

