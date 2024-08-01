# setbuf()函数

```c
void setbuf(FILE *stream, char *buffer)
```

* 解释：设置用于流操作的内部缓冲区。它应该至少有BUFSIZ个字符长
* 参数：
  * **stream** -- 这是指向 FILE 对象的指针，该 FILE 对象标识了一个打开的流。
  * **buffer** -- 这是分配给用户的缓冲，buffer为缓冲区的起始地址,它的长度至少为 BUFSIZ 字节，BUFSIZ 是一个宏常量，表示数组的长度。
  * 如果*缓冲*是一个空指针，为该缓冲区禁用了缓冲*流*，成为*无缓冲*流。
* 头文件：`#include <stdio.h>`