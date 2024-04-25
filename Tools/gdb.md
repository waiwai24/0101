# gdb



## 1.启动调试

> 对于C程序而言，需要在编译时加上`-g`参数，保留调试信息，否则不能使用gdb进行调试

例如：

```text
$ gdb helloworld
Reading symbols from helloWorld...(no debugging symbols found)...done.
```

如果没有调试信息，会提示no debugging symbols found。
如果是下面的提示：

```text
Reading symbols from helloWorld...done.
```

则可以进行调试。

同样使用`file`命令也可以看出有无debug信息，并且如果最后是stripped则说明该文件的符号表信息和调试信息被去除，不能使用gdb调试，但是not stripped的情况并不能说明能够被调试

```shell
┌──(waiwai㉿kali)-[/home/ctf/pwn/int_overflow]
└─$ file a.out 
a.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=612336f334e5e5d4b5775e89a8c1716c5eac0ee0, for GNU/Linux 3.2.0, with debug_info, not stripped
                                                                                                                                        
┌──(waiwai㉿kali)-[/home/ctf/pwn/int_overflow]
└─$ file b.out
b.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e401563630cf931a9f85530f828e98030b01b317, for GNU/Linux 3.2.0, not stripped
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

  

## 2.断点设置

* 根据行号设置：b num

* 根据函数名设置：b func

* 根据条件设置： break test.c:23 if b==0 (当b为0时会在23行断住)

* 设置临时断点：tbreak test.c:23

* 跳过多次设置断点：ignore 1 30 (1是忽略的断点号，30是要跳过的次数)

* 根据表达式值变化产生断点：watch a (观察a值是否变化，前提是程序必须运行起来)

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

* 打印print基本类型变量，数组，字符：p a(变量名)，p ‘main’::a
* 打印指针指向内容：
  * p *d  (如果不加\*则打印出指针地址)（打印出第一个值）
  * p *d@10  (解引用打印多个值@后跟上要打印的长度或变量值)



## 4.单步调试

## 5.源码查看

6.