# write() & fwrite()

## 1.write()

```c
ssize write(int fd,const void * buf,size_t count);
```

* 头文件：#include <unistd.h>
* write()会把参数buf所指的内存写入count个字节到参数fd所指的文件内
* fd: 文件描述符。
* buf: 定义的缓冲区，是一个指针，指向一段内存。
* count: 写入文件的字节数。
* 返回值：成功返回写入文件的字节数，失败返回-1



## 2.fwrite()

```c
size_t fwrite(const void *ptr, size_t size, size_t number, FILE *stream)
```

* 头文件：#include<stdio.h> 

* ptr：这是指向要被写入的元素数组的指针。
* size：这是要被写入的每个元素的大小，以字节为单位。
* number：这是元素的个数，每个元素的大小为 size 字节。
* stream：这是指向 FILE 对象的指针，该 FILE 对象指定了一个输出流。
* size_t 返回值返回的是实际写出到文件的基本单元个数