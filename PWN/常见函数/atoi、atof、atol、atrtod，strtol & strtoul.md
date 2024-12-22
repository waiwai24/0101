# atoi、atof、atol、atrtod，strtol & strtoul

头文件 

```c
#include<stdlib.h>
```



## 1.atoi

```c
int atoi(const  char *  nptr);
```

* atoi()会扫描参数nptr字符串，跳过前面的空格字符，直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回
* 返回值：返回转换后的整型数
* itoa（把一整数转换为字符串 ）



## 2.atof

```c
double atof(const char *nptr);
```

* atof()会扫描参数nptr字符串，跳过前面的空格字符，直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回
* 参数nptr字符串可包含正负号、小数点或E(e)来表示指数部分，如123.456或123e-2。返回值 返回转换后的浮点型数
  



## 3.atol

```c
long atol(const char \*nptr);
```

* atol()会扫描参数nptr字符串，跳过前面的空格字符，直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回