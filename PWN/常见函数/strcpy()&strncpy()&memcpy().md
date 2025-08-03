# strcpy() & strncpy() & memcpy()

## 1.strcpy()

```c
char *strcpy(char* dest, const char *src);
```

* \#include <string.h> 和 #include <stdio.h>
* 把从src地址开始且**含有NULL结束符**的字符串复制到以dest开始的地址空间
* 遇到 `\0`（ascii码为0）的时候马上结束
* 返回一个指向最终的目标字符串 dest 的指针
* 注：dest的空间必须要能够存储src的长度加上NULL字符



## 2.strncpy()

```c
char * strncpy（char * dest，const char * src，size_t n
```

* strncpy()不会向dest追加结束标记’\0’，这就引发了很多不合常理的问题，后续对于字符串的操作可能会造成内存的非法访问



## 3.memcpy()

```c
void *memcpy(void *str1, const void *str2, size_t n)
```

* #include <string.h>
* 从存储区 str2 复制 n 个字节到存储区 str1
* 返回一个指向目标存储区 str1 的指针
* 相较于 strcpy() 函数，memcpy函数遇到  \x00 将会继续复制，不发生 00 截断