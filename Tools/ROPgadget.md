# ROPgadget



## 1.介绍

随着 NX 保护的开启，以往直接向栈或者堆上直接注入代码的方式难以继续发挥效果。攻击者们也提出来相应的方法来绕过保护，目前主要的是 ROP(Return Oriented Programming)，其主要思想是在栈缓冲区溢出的基础上，利用程序中已有的小片段 (gadgets) 来改变某些寄存器或者变量的值，从而控制程序的执行流程。所谓 gadgets 就是以 ret 结尾的指令序列，通过这些指令序列，我们可以修改某些地址的内容，方便控制程序的执行流程



## 2.用法

64位汇编传参，当参数少于7个时， 参数从左到右放入寄存器: rdi, rsi, rdx, rcx, r8, r9。 当参数为7个以上时，前 6 个与前面一样， 但后面的依次从 “右向左” 放入栈中，即和32位汇编一样

```
ROPgadget --binary 文件名 --only "pop|ret" | grep rdi
ROPgadget --binary 文件名 --only "pop|ret"
ROPgadget --binary 文件名 --string '/sh'
```

