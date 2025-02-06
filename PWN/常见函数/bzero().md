# bzero()

```c
 void bzero(void *s, int n);
```

* 头文件：#include <string.h>
* bzero() 会将内存块（字符串）的前n个字节清零
* bzero(void *s, int n) 等价于 memset((void*)s, 0,size_tn)，用来将内存块的前 n 个字节清零