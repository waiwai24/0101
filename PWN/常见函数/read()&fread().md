# read() & fread()

> ssize_t：有符号整型，与long类似。typedef long size_t
>
> size_t：无符号的ssize_t,：typedef unsigned long size_t

## 1.read()

```c
ssize_t read(int fd, void *buf, size_t count)
```

* 读取打开文件的count字节保存到buf缓冲区，返回实际读取的字节数
* 头文件：#include <unistd.h>
* fd=0，代表标准输入流；File Descriptor (FD)：stdin = 0、stdout = 1、stderr = 2
* 文件描述符（file descriptor）。文件描述符只是一个整数，是每个进程私有的，在 UNIX 系统中用于访问文件。因此，一旦文件被打开，就可以使用文件描述符来读取或写入文件
* 在orw中，read第一个打开文件的文件描述符必定是3，后面打开的文件以此类推4，5...
* 每个正在运行的进程已经打开了 3 个文件：标准输入（进程可以读取以接收输入），标准输出（进程可以写入以便将信息显示到屏幕），以及标准错误（进程可以写入错误消息）。这些分别由文件描述符 0、1 和 2 表示。因此，当你第一次打开另一个文件时（如上例所示），它几乎肯定是文件描述符 3



## 2.fread()

```c
size_t fread(void *ptr, size_t size, size_t count, FILE *stream);
```

- fread() 函数可以从文件中读取二进制数据。它在读取数据时，会从文件流中读取 count 个数据项，每个数据项占用 size 个字节。它会将这些数据项存储到由 ptr 指向的缓冲区中，并返回成功读取的数据项数目
- 头文件 ：#include<stdio.h>
- ptr：指向要读取数据的缓冲区
- size：每个数据项的字节数
- count：要读取的数据项数目
- stream：指向文件流的指针

