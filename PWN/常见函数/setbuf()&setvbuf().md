# setbuf() & setvbuf()

## 1.setbuf()

```c
void setbuf(FILE *stream, char *buffer)
```

* 头文件：`#include <stdio.h>`
* 解释：设置用于流操作的内部缓冲区。它应该至少有BUFSIZ个字符长
* 参数：
  * **stream** -- 这是指向 FILE 对象的指针，该 FILE 对象标识了一个打开的流。
  * **buffer** -- 这是分配给用户的缓冲，buffer为缓冲区的起始地址,它的长度至少为 BUFSIZ 字节，BUFSIZ 是一个宏常量，表示数组的长度。
  * 如果*缓冲*是一个空指针，为该缓冲区禁用了缓冲*流*，成为*无缓冲*流。



## 2.setvbuf()

```c
int setvbuf(FILE *stream, char *buffer, int mode, size_t size)
```

- 参数：

  - **stream** -- 这是指向 FILE 对象的指针，该 FILE 对象标识了一个打开的流。

  - **buffer** -- 这是分配给用户的缓冲。如果设置为 NULL，该函数会自动分配一个指定大小的缓冲。

  - **mode** -- 这指定了文件缓冲的模式：

    - `_IOFBF`：完全缓冲

    - `_IOLBF`：行缓冲

    - `_IONBF`：没有缓冲

    - ```c
      #define _IOFBF 0 /* Fully buffered. */
      #define _IOLBF 1 /* Line buffered. */
      #define _IONBF 2 /* No buffering. */
      ```

  - **size** --这是缓冲的大小，以字节为单位。

- 如果成功，则该函数返回 0，否则返回非零值