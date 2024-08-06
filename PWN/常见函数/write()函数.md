# write()函数

```
ssize write(int fd,const void * buf,size_t count);
```

* 头文件：#include <unistd.h>
* fd: 文件描述符。
* buf: 定义的缓冲区，是一个指针，指向一段内存。
* count: 写入文件的字节数。
* 返回值：成功返回写入文件的字节数，失败返回-1