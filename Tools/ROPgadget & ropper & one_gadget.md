# ROPgadget & ropper & one_gadget



## 1.介绍

随着 NX 保护的开启，以往直接向栈或者堆上直接注入代码的方式难以继续发挥效果。攻击者们也提出来相应的方法来绕过保护，目前主要的是 ROP(Return Oriented Programming)，其主要思想是在栈缓冲区溢出的基础上，利用程序中已有的小片段 (gadgets) 来改变某些寄存器或者变量的值，从而控制程序的执行流程。所谓 gadgets 就是以 ret 结尾的指令序列，通过这些指令序列，我们可以修改某些地址的内容，方便控制程序的执行流程



## 2.ROPgadget用法

64位汇编传参，当参数少于7个时， 参数从左到右放入寄存器: rdi, rsi, rdx, rcx, r8, r9。 当参数为7个以上时，前 6 个与前面一样， 但后面的依次从 “右向左” 放入栈中，即和32位汇编一样

```
ROPgadget --binary 文件名 --only "pop|ret" | grep rdi
ROPgadget --binary 文件名 --only "pop|ret"
ROPgadget --binary 文件名 --string '/bin/sh'
```

```
usage: ROPgadget [-h] [-v] [-c] [--binary <binary>] [--opcode <opcodes>]
                 [--string <string>] [--memstr <string>] [--depth <nbyte>]
                 [--only <key>] [--filter <key>] [--range <start-end>]
                 [--badbytes <byte>] [--rawArch <arch>] [--rawMode <mode>]
                 [--rawEndian <endian>] [--re <re>] [--offset <hexaddr>]
                 [--ropchain] [--thumb] [--console] [--norop] [--nojop]
                 [--callPreceded] [--nosys] [--multibr] [--all] [--noinstr]
                 [--dump] [--silent] [--align ALIGN] [--mipsrop <rtype>]

参数详解

-h, --help           显示帮助文档
-v, --version        版本号
-c, --checkUpdate    检测新版本是否可用
--binary <binary>    指定二进制文件进行分析
--opcode <opcodes>   在可执行段中查找opcode
--string <string>    在可读的段中查找字符串
--memstr <string>    查找单个byte在所有的可执行段中
--depth <nbyte>      搜索引擎的深度(默认10)
--only <key>         只显示特别的指令
--filter <key>       过滤特定指令
--range <start-end>  在地址之间寻找(0x...-0x...)
--badbytes <byte>    拒绝特定指令在gadget的地址下
--rawArch <arch>     指定文件架构: x86|arm|arm64|sparc|mips|ppc
--rawMode <mode>     指定源文件的mode: 32|64|arm|thumb
--rawEndian <endian> 指定源文件的字节顺序: little|big
--re <re>            正则表达式
--offset <hexaddr>   指定gadget的地址偏移
--ropchain           ROP链的生成
--thumb              在ARM架构下使用搜索引擎thumb 模式
--console            使用交互终端对于搜索引擎
--norop              禁止ROP搜索引擎
--nojop              禁止JOP搜索引擎
--callPreceded       仅显示call-preceded的gadgets
--nosys              禁止SYS搜索引擎
--multibr            允许多分枝gadgets
--all                禁止删除重复的gadgets，即显示所有
--noinstr            禁止gadget指令终端打印
--dump               输出gadget bytes
--align ALIGN        对齐gadget地址（以字节为单位）
--mipsrop <rtype>    MIPSj架构下有用的gadget查找器: stackfinder|system|tails|lia0|registers
```



## 3.ropper用法

```
直接ropper进入界面
file 指定文件
search 搜索
```



## 4.one_gadget

```shell
$ one_gadget libc-2.23.so

0x45226 execve("/bin/sh", rsp+0x30, environ)
constraints:
  rax == NULL                                # 这个提示的意思就是在调用one_gadget前需要满足的条件

0x4527a execve("/bin/sh", rsp+0x30, environ)
constraints:
  [rsp+0x30] == NULL

0xf03a4 execve("/bin/sh", rsp+0x50, environ)
constraints:
  [rsp+0x50] == NULL
```

* one_gadget是libc中存在的一些执行`execve("/bin/sh", NULL, NULL)`的片段，当可以泄露libc地址，并且可以知道libc版本的时候，可以使用此方法来快速控制指令寄存器开启shell。

* 相比于`system("/bin/sh")`，这种方式更加方便，不用控制RDI、RSI、RDX等参数。运用于不利构造参数的情况
* **注意**：one_gadget并不总是可以获取shell，它首先要满足一些条件才能执行成功

