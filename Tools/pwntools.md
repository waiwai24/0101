# pwntools

```python
from pwm import *
```

注意：py3使用时确保所有字符串都有个`b`前缀，因为但是python2的str类型时bytes类型，但python3时是Unicode类型，和bytes类型有区别

tips：使用ipython可以方便查看各自模块和函数的详细使用用法`? name`



## 1.tubes

主要函数在 `pwnlib.tubes.tube`,子模块只实现某管道特殊的地方。四种管道和相对应的子模块如下

四种管道：

* 进程：`p=process("/bin/sh")`

* 套接字： `l=listen(1080)`，`r=remote('1270.0.1',1080)`

* SSH ：`s=ssh(host='example.com',user='name',password='passwd')`

* 串口：`pwnlib.tubes.serialtube`

  tips:串口通信是指外设和计算机间，通过数据信号线 、地线、控制线等，按位进行传输数据的一种通讯方式

`pwnlib.tubes.tube` 中的主要函数：

* `interactive()`：同时读写管道，相当于回到 shell 模式进行交互，在取得 shell 之后调用
* `recv(num,timeout=default)`：接收指定数量的可用字节
* `recvall()`：接受数据直到EOF
* `recvline()`：接受一行数据
* `recvuntil(delims, timeout=default)`：接收数据直到 delims 出现
* `send(data)`：发送数据
* `sendline(data)`：发送一行数据，默认在行尾加\n
* `close()`：关闭管道





## 2.pack&unpack

打包/解包任意长度的整数，默认小端，添加参数`endian`,`signed`可以设置端序和是否带符号 

* `p16()`，`p32()`：打包16/32位的整数
* `u16()`，`u32()`：解包16/32位的整数



## 3.哈希和编码

* `b64e()`，`b64d()`
* `md5sumhex()`，`md5filehex()`，
* `sha1sumhex()`
* `enhex`,`unhex`



## 4.shellcraft

使用 shellcraft 模块可以生成对应架构和 shellcode 代码，直接使用链式调用的方法就可以得到，首先指定体系结构，再指定操作系统

示例：

```python
>>> print(shellcraft.i386.linux.sh())
    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push '/bin///sh\x00' */
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00\x00' */
    push 0x1010101
    xor dword ptr [esp], 0x1016972
    xor ecx, ecx
    push ecx /* null terminate */
    push 4
    pop ecx
    add ecx, esp
    push ecx /* 'sh\x00' */
    mov ecx, esp
    xor edx, edx
    /* call execve() */
    push SYS_execve /* 0xb */
    pop eax
    int 0x80
```



## 5.asm

用于汇编和反汇编

体系结构，端序和字长需要在 `asm()` 和 `disasm()` 中设置，但为了避免重复，运行时变量最好使用 `pwnlib.context` 来设置

```python
>>> asm(shellcraft.nop()) ;i386架构下
'\x90'
>>> asm('nop', arch='arm')
'\x00\xf0 \xe3'
>>> context.arch = 'arm'
>>> context.os = 'linux'
>>> context.endian = 'little'
>>> context.word_size = 32
>>> context
ContextType(arch = 'arm', bits = 32, endian = 'little', os = 'linux')
```

```python
>>> print(disasm(b'\xb8\x01\x00\x00\x00'))
   0:   b8 01 00 00 00          mov    eax, 0x1
```



## 6.联动GDB调试
