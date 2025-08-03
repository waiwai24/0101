# atoi() & atol() & strtol() & strtoll() & strtoul() & strtoull()



```c
int atoi(const  char *  nptr);
```

* atoi()会扫描参数nptr字符串，跳过前面的空格字符，直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回
* 返回值：返回转换后的整型数
* itoa（把一整数转换为字符串 ）



```c
double atof(const char *nptr);
```

* atof()会扫描参数nptr字符串，跳过前面的空格字符，直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回
* 参数nptr字符串可包含正负号、小数点或E(e)来表示指数部分，如123.456或123e-2。返回值 返回转换后的浮点型数



```c
long atol(const char \*nptr);
```

* atol()会扫描参数nptr字符串，跳过前面的空格字符，直到遇上数字或正负符号才开始做转换，而再遇到非数字或字符串结束时('\0')才结束转换，并将结果返回



```c
 #include <stdlib.h>
 long int strtol(const char *nptr, char **endptr, int base);
 long long int strtoll(const char *nptr, char **endptr, int base);
 unsigned long int strtoul(const char *nptr, char **endptr, int base);
 unsigned long long int strtoull(const char *nptr, char **endptr, int base);
```

* 对类型为 char* 的对象的引用，其值由函数设置为 **str** 中数值后的下一个字符
* 这一组函数根据指定的进制base(2-36或者0，为0时根据字符串自动推断转换的进制)将nptr指向的字符串转换为对应的整形
* 函数返回被转换的长整型整数值。如果输入字符串不符合数字格式，strtol() 将返回 0





