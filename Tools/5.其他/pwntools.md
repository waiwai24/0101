# pwntools

```python
from pwm import *
```

注意：py3使用时确保所有字符串都有个`b`前缀，因为python2的str类型是bytes类型，但python3时是Unicode类型，和bytes类型有区别

tips：使用ipython可以方便查看各自模块和函数的详细使用用法`? name`



## 1.tubes

主要函数在 `pwnlib.tubes.tube`,子模块只实现某管道特殊的地方。四种管道和相对应的子模块如下

四种管道：

* 进程：`p=process("/bin/sh")`

* 套接字：`l=listen(1080)`，`r=remote('1270.0.1',1080)`

* SSH ：`session=ssh(host='example.com',port=22，user='name',password='passwd')`

* 串口：`pwnlib.tubes.serialtube`

  tips:串口通信是指外设和计算机间，通过数据信号线 、地线、控制线等，按位进行传输数据的一种通讯方式

交互：

* `interactive()`：同时读写管道，相当于回到 shell 模式进行交互，在取得 shell 之后调用

接收数据：

* `recv(num,timeout=default)`：接收指定数量的可用字节
* `recvall()`：接受数据直到EOF
* `recvline()`：接受一行数据直到遇到换行，设置参数 keepends = False 可不保留 \n
* `recvuntil(delims, timeout=default)`：接收数据直到 delims 出现
* `recvrepeat(timeout)`：继续接收数据，直到发生超时
* `clean()`：丢弃所有缓冲的数据

发送数据

* `send(data)`：发送数据
* `sendline(data)`：发送一行数据，默认在行尾加\n，也就是0xa
* `sendafter(some_string, payload)`：接收到 some_string 后, 发送你的 payload
* `close()`：关闭管道



## 2.pack&unpack

打包/解包任意长度的整数，默认小端，添加参数`endian`,`signed`可以设置端序和是否带符号 

* `p16()`，`p32()`：打包16/32位的整数，将整数打包为相对应位数的地址表示方式
* `u16()`，`u32()`：解包16/32位的整数，把\x\x码重新变为整数

```python
>>> p32(0xdeadbeef)
'\xef\xbe\xad\xde'
>>> p64(0xdeadbeef).encode('hex')
'efbeadde00000000'
>>> p32(0xdeadbeef, endian='big', sign='unsigned')
'\xde\xad\xbe\xef'
```



## 3.哈希和编码

* `b64e()`，`b64d()`
* `md5sumhex()`，`md5filehex()`，
* `sha1sumhex()`
* `enhex`,`unhex`
* `urlencode()` 



## 4.shellcraft

使用 shellcraft 模块可以生成对应架构和 shellcode 代码，直接使用链式调用的方法就可以得到，首先指定体系结构，再指定操作系统

示例：

```python
from pwn import *
help(shellcraft.sh)
print '---'
print shellcraft.sh()
print '---'
print enhex(asm(shellcraft.sh()))
```

```python
Help on function sh in module pwnlib.shellcraft.internal:
sh()
Execute /bin/sh
---
/* push '/bin///sh\x00' */
push 0x68
push 0x732f2f2f
push 0x6e69622f
/* call execve('esp', 0, 0) */
push (SYS_execve) /* 0xb */
                    pop eax
mov ebx, esp
xor ecx, ecx
cdq /* edx=0 */
int 0x80
---
6a68682f2f2f73682f62696e6a0b5889e331c999cd80
```



## 5.asm

用于汇编和反汇编

* `asm()`汇编

  ```
  asm('mov eax, 0')
  '\xb8\x00\x00\x00\x00'
  ```

* `disasm()`反汇编

  ```
  disasm('\xb8\x0b\x00\x00\x00')
  '  0: b8 0b 00 00 00        mov  eax,0xb'
  ```

体系结构，端序和字长需要在 `asm()` 和 `disasm()` 中设置，但为了避免重复，运行时变量最好使用 `pwnlib.context` 来设置

```python
context(arch='amd64', os='linux', endian='little')
context.log_level = "debug" # 打印调试信息
context.log_level = "error" # 打印错误信息, 此时很多回显就看不到了
context.log_level = "info"  #默认
```



## 6.联动GDB调试

```python
启动一个进程，并且停在第一条指令(推荐使用)
io = gdb.debug("/bin/bash", gdbscript='continue')

附加到一个进程，target可以是pid也可以是process
gdb.attach(target, gdbscript=None)
gdb.attach(proc.pidof(p)[0])
pause()
```

在脚本中调用 gdb 并不是准确停在调用这一行，而是会执行到脚本的 下一（或几）行，举个例子：



## 7.ELF

ELF文件有几组不同的符号表可用，每组都包含在`{name: data}`的字典中

- `ELF.symbols[]` 列出所有已知的符号，包括下面的符号(符号可以是变量、函数、或其他常量)。优先考虑PLT条目，而不是GOT条目。
- `ELF.got[]` 只包含GOT表
- `ELF.plt[]` 只包含PLT表
- `ELF.functions` 只包含函数符号表（需要DWARF符号表）

```python
>>> e = ELF('/bin/cat')
[*] '/bin/cat'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
>>> print hex(e.address) 
#文件装载基地址,如果二进制文件没有启用PIE，那么它是绝对地址;如果启用了，所有地址都是相对地址
#设置address值会自动更新symbols、got、plt和functions的地址，这使得它在调整PIE或ASLR时非常有用
0x400000
>>> print hex(e.symbols['write'])
0x401680
>>> print hex(e.got['write'])
0x60b070
>>> print hex(e.plt['write'])
0x401680
```



## 8.其他

* `cyclic(len)`：生成指定长度的数据
* `cyclic -l lookup_value`:执行查找
* `b *$rebase(0x相对基址偏移)` 是 pwngdb 中的一个调试命令，用于在基地址重定位后设置断点
* `flat`函数可以将一个列表（或其他可迭代对象）中的元素转换为二进制字符串，并将这些字符串连续拼接起来。这对于在二进制漏洞利用中构造包含多个数据块的payload特别有用

  ```python
  In [1]: flat([1,2],endianness = 'little', word_size = 32, sign = False)                                                       Out[1]: b'\x01\x00\x00\x00\x02\x00\x00\x00'
  
  In [2]: flat([1,2],word_size=64)                                                                                             Out[2]: b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00'
  ```
* `log.info()`：打印状态信息
* `FmtStr(execute_fmt, offset=None, padlen=0, numbwritten=0)`

  * execute_fmt(function)：与漏洞进程进行交互的函数；
  * offset(int)：控制的第一个格式化程序的偏移量
  * padlen(int)：在payload之前添加的pad的大小
  * numbwritten(int)：已经写入的字节数
* `fmtstr_payload(offset, {address:data}, numbwritten=0, write_size='byte')`
  * 自动生成格式化字符串 paylod
  * offset 表示格式化字符串的偏移
  * {address:data} 表示在address写入data
  * numbwritten 表示已经输出的字符个数
  * write_size 表示写入方式，是按字节（byte）、按双字节（short）还是按四字节（int），对应着hhn、hn和n，默认值是byte，即按hhn写
