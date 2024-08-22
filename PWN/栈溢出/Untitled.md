没有nx：

* 自带system('/bin/sh')，直接覆盖返回地址
* 可以找到system函数的plt绝对地址，ret2text
* 找不到system，利用输入函数，shellcode写入程序，ret2shellcode

有nx：

* ROPgadget配合系统调用execve：ret2syscall
* 利用libc获取system和bin/sh：ret2libc