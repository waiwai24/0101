# gdb



## 1.启动调试

> 对于C程序而言，需要在编译时加上`-g`参数，保留调试信息，否则不能使用gdb进行调试，使用enter键可重复执行上一条指令命令

例如：

```text
$ gdb helloworld
Reading symbols from helloWorld...(no debugging symbols found)...done.
```

如果没有调试信息，会提示no debugging symbols found。
如果有则是下面的提示：

```text
Reading symbols from helloWorld...done.
```

则可以进行调试。

同样使用`file`命令也可以看出有无debug信息，并且如果最后是stripped则说明该文件的符号表信息和调试信息被去除，不能使用gdb调试，但是not stripped的情况并不能说明能够被调试

```shell
┌──(waiwai㉿kali)-[/home/ctf/pwn/int_overflow]
└─$ file a.out 
a.out： ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=612336f334e5e5d4b5775e89a8c1716c5eac0ee0, for GNU/Linux 3.2.0, with debug_info, not stripped
                                                                                                                                        
┌──(waiwai㉿kali)-[/home/ctf/pwn/int_overflow]
└─$ file b.out
b.out： ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e401563630cf931a9f85530f828e98030b01b317, for GNU/Linux 3.2.0, not stripped
```

* 调试无参数程序： 

  ```bash
  gdb file.o
  (gdb) run
  ```

* 调试带参程序：

  ```bash
  gdb file.o
  (gdb) run arg
  ```

* 调试已运行程序：先找到进程id再attach

  ```shell
  ps -ef|grep 进程名
  gdb
  (gdb) attach pid
  ```

* run 指令会一直执行程序，直到执行结束

* start 指令会执行程序至 main() 主函数的起始位置，即在 main() 函数的第一行语句处停止执行（该行代码尚未执行）

* starti 开始执行程序，在第一条指令处会停下来

* 程序执行过程中使用 run 或者 start 指令，表示的是重新启动程序

日志记录：

```shell
set logging file gdb_log.txt  
set logging on  
```



## 2.断点设置

* 根据行号设置：b num

* 根据函数名设置：b func

* 根据地址设置：b *0x12345678

* 根据条件设置： break test.c：23 if b==0 (当b为0时会在23行断住)

* 设置临时断点：tbreak test.c：23

* 跳过多次设置断点：ignore 1 30 (1是忽略的断点号，30是要跳过的次数)

* 内存监控：

  * 根据表达式值变化产生断点：watch a (观察a值是否变化，前提是程序必须运行起来)
  * watch *(void/int/char...... *)(内存地址)/全局变量名，为表达式（变量）expr设置一个观察点。一量表达式值有变化时，立马停住
  * rwatch <expr>，当表达式（变量）expr被读时，停住程序
  * awatch <expr>，当表达式（变量）的值被读或被写时，停住程序
  * info watchpoints，列出当前所设置了的所有观察点

* 禁用/启用断点：

  * disable：禁用所有
  * disable num：禁用标号num的断点
  * enable：启用所有断点
  * enable num：启用标号num断点
  * enable delete num：启动标号num的断点，并且在此之后删除该断点

* 断点清除：

  * clear：删除所有b
  * clear func：删除函数func断点
  * delete：删除所有breakpoints，watchpoints，catchpoints
  * delete num：删除num号断点

  

## 3.变量查看

* 打印print基本类型变量，数组，字符：p a(变量名)，p ‘main’：：a
* 打印指针指向内容：
  * p *d  (如果不加\*则打印出指针地址)（打印出第一个值）
  * p *d@10  (解引用打印多个值@后跟上要打印的长度或变量值)
* 按照特定格式打印变量：
  * x 十六进制格式
  * d 十进制格式
  * u 十六进制格式显示无符号整型
  * c 按字符格式
  * f 按浮点数格式 
  * t 按二进制格式


```
(gdb) p c
$18 = "hello,shouwang"
(gdb) p/x c
$19 = {0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x73, 0x68, 0x6f, 0x75, 0x77, 0x61, 0x6e, 0x67, 0x0}

```

* 查看内存内容：
  * 语法：`x/[n][f][u] addr`,x：examine检查内存
  
  * n：要显示的内存单元数，默认为1
  
  * f：表示要打印的格式
  
    ```
      x 按十六进制格式显示变量。
      d 按十进制格式显示变量。
      u 按十进制格式显示无符号整型。
      o 按八进制格式显示变量。
      t 按二进制格式显示变量。
      a 按十六进制格式显示变量。
      i 指令地址格式
      c 按字符格式显示变量。
      f 按浮点数格式显示变量。
    ```
  
  * u：要打印的一个地址的单元长度
  
    ```
    b表示单字节，
    h表示双字节，
    w表示四字节，
    g表示八字节
    ```
  
  * addr：内存地址

    ```
	  (gdb) x/4tb &e
	  0x7fffffffdbd4：    00000000    00000000    00001000    01000001
	  变量e的四个字节都以二进制的方式打印出来了
    ```

* info registers：打印普通寄存器	

* info all-registers：打印所有寄存器

* 查看函数：info functions

* 直接调用函数执行：call function 或 print function

* set 修改运行时变量内容，也可以直接set地址指定的值

  ```
  set var variable=value
  ```
  
* 设定程序运行时的参数

  ```
  set args arg1 arg2 ...
  ```

* set一般只能修改4字节，如果要修改8字节，就要强制类型转换

  例子：`set *(long long*)0x7fffffffdf18=0x1234567812345678` 的意思是：将内存地址 `0x7fffffffdf18` 强制解释为一个 `long long` 类型的指针，然后通过间接引用操作符 `*` 来访问或修改这个地址处的 `long long` 值
  
  

## 4.单步调试

* 单步执行next，简写n，用于程序断住后，继续执行下一条语句，后面跟上数字num，表示执行该命令num次,当你执行到某个函数时，不会进入该函数内部，而是直接执行完该函数，然后继续执行下一行代码。

* 单步进入step，简写s，可以单步跟踪到函数内部

* 继续执行到下一个断点continue，简写c，他会执行程序直到再次遇到断点处

* until（简写u）：当你厌倦了在一个循环体内单步跟踪时，这个命令可以运行程序直到退出循环体
  until+行号： 运行至某行，不仅仅用来跳出循环
  
* finish 继续执行直到当前选定栈帧上的函数返回

* return 取消函数调用的执行

  return expression 如果指定一个 expression 表达式参数，其值将是此函数的返回值

```
next   单步到程序源代码的下一行，不进入函数。
nexti （ni）单步一条机器指令，不进入函数。
step   单步到下一个不同的源代码行（包括进入函数）。
stepi （si）单步一条机器指令。
```

* reverse-调试方法，可以反向调试（但是要在此之前开启record full）



## 5.源码查看

* list：将源码列出来，简写l
  * 后面可以跟行号，表示要列出附近的源码
  * 后面跟函数名，列出指定函数附近的源码
  * 设置源码一次列出行数，set listsize num
  * 列出指定行之间的源码，list first，last



## 6.反汇编

反汇编只能在运行过程中使用

* 反汇编main函数

  ```
  disassemble main
  disass main
  ```



## 7.堆相关

* `vis_heap_chunks [count] [address]`：简写vis，在指定的地址上可视化堆块

* `arena`：显示arena的详细信息,过于详细

* `p main_arena`:主线程
* `arenas`：显示所有arena的基本信息

* `arenainfo`：好看的显示所有arena的信息

- `bins`：查看所有种类的堆块的链表情况
- `fastbins`：单独查看fastbins的链表情况
- `largebins`：同上，单独查看largebins的链表情况
- `smallbins`：同上，单独查看smallbins的链表情况
- `unsortedbin`：同上，单独查看unsortedbin链表情况
- `tcachebins`：同上，单独查看tcachebins的链表情况
- `tcache`：查看tcache详细信息
- `heap`：数据结构的形式显示所有堆块，会显示一大堆
- `heap -v`：查看完整数据结构
- `parseheap`，`par`：显示堆结构，很好用，与heap大同小异
- `mp`：查看堆相关结构体信息
- `heapbase`：查看堆起始地址
- `heapinfo、heapinfoall`：显示堆的信息，和bins的挺像的，没bins好用
- `tracemalloc`：好用，会跟提示所有操作堆的地方
- `try_free`：检查堆管理器是否能释放gai



## 8.多线程调试

* `info threads`: 查看当前所有的线程
* `thread n`: 切换到 id 为n的线程中
* 对于进程也有类似的命令`info inferiors`/`inferior n`
* `set detach-on-fork on`：设置gdb是否分离fork的子进程，默认on
* `set follow-fork-mode child`：设置调试器响应到fork或vfork的程序调用,默认跟踪parent进程
* `catch exec`：捕获对 exec 的调用
* `catch fork`：捕获对 fork 的调用
* `catch vfork`：捕获对 vfork 的调用
* `catch syscall`：捕获系统调用



## 9.插件及其他

* 代码分屏快捷键：ctrl x + a
* show debug-file-directory
* set debug-file-directory directories：指定带调试信息共享库所在目录，也就是对应glibc版本的.debug目录，方法只是该次有效，当重新gdb调试时需要再次设置
* 查看源码搜索路径：show directories
* directory path：指定源文件目录(源码调试时)（通常指定glibc源码路径），也可以在开始gdb时使用 gdb -d path 指定源文件路径
* layout：用于分割窗口，可以一边查看代码，一边测试。主要有以下几种用法：
* layout src：显示源代码窗口
* layout asm：显示汇编窗口
* layout regs：显示源代码/汇编和寄存器窗口
* layout split：显示源代码和汇编窗口
* layout next：显示下一个layout
* layout prev：显示上一个layoutCtrl + L：刷新窗口
* Ctrl + x，再按1：单窗口模式，显示一个窗口
* Ctrl + x，再按2：双窗口模式，显示两个窗口
* Ctrl + x，再按a：回到传统模式，即退出layout，回到执行layout之前的调试窗口
* Ctrl + r，指令反向搜索
* backtrace：(简写bt)可以查看程序的调用栈。-full 参数可完整打印
* !shell：执行shell命令
* search -t {type} value
* find start_addr,end_addr,value
* source file，运行file里面的脚本
* u：在指定地址附近反汇编
* hex：查看地址处的数据
* leakfind addr --page_name=heap --max_offset=0x3000 --max_depth=3：尝试根据起始地址查找泄漏链，默认在栈中扫描，offset指定范围，depth指定深度

### 9.1 pwndbg

* `b *$rebase(偏移)`：PIE开启情况下下断点

* `codebase`：打印PIE偏移

* `telescope -addr count`：从指定地址开始递归地解引用指针（默认为$esp），计数值默认为8

* `vmmap`：查看程序各种段的地址和范围

* `cyclic n`：生成的字符串每四个字符为一组，以aaaa开始，最长到zzzz

  ```
  $ cyclic 128    
  aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaab
  ```

  ```
  可计算出栈溢出的长度
  pwndbg> cyclic -l 'gaaa'
  24
  ```

* `fmtarg addr`:在进入`printf`函数时断下，调用`fmtarg`后可以自动计算格式化参数与`addr`的偏移

* 程序运行时对参数的输入/控制：

  * run后面直接跟参数
  * `set args`
  * 标准输入：`run < file`,`$ python -c 'print "A"*100' | ./demo`,`run < <(python -c 'print "A"*100')`
