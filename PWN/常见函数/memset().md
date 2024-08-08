# memset()



```c
void *memset(void *str, int c, size_t n)
```

- 解释：复制字符 c（一个无符号字符）到参数 str 所指向的字符串的前 n 个字符。
- 作用：是在一段内存块中填充某个给定的值，它是对较大的结构体或数组进行清零操作的一种最快方法
- 头文件：C中`#include<string.h>`，C++中`#include<cstring>`

* 注意：memset赋值的时候是按字节赋值，是将参数化成二进制之后填入一个字节

