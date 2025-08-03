# getc() & putc()

## 1.getc()

```c
int getc(FILE *stream)
```

* 头文件 #include<stdio.h>
* 从指定的流 stream 获取下一个字符（一个无符号字符），并把位置标识符往前移动
* 返回值：该函数以无符号 char 强制转换为 int 的形式返回读取的字符，如果到达文件末尾或发生读错误，则返回 EOF



## 2.putc()

```c
int putc(int char, FILE *stream)
```

* 头文件 #include<stdio.h>
* 把参数 char 指定的字符（一个无符号字符）写入到指定的流 stream 中，并把位置标识符往前移动

* 返回值：该函数以无符号 char 强制转换为 int 的形式返回写入的字符，如果发生错误则返回 EOF