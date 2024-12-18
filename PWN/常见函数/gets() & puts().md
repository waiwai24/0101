# gets() & puts()

## 1.gets()

```c
char *gets(char *str)
```

* 头文件：`#include <stdio.h>`
* 从标准输入 stdin 读取一行，并把它存储在 str 所指向的字符串中。当读取到换行符时，或者到达文件末尾时，它会停止
* 危险函数，不会对用户输入的数据长度进行限制
* `strlen()`函数来判断输入的长度，遇到`'\x00'`时会终止，而`gets()`函数遇到`'\x00'`并不会截断
* 返回：如果成功，该函数返回 str。如果发生错误或者到达文件末尾时还未读取任何字符，则返回 NULL



## 2.puts()

```c
int puts(const char *str)
```

* 头文件：`#include <stdio.h>`
* 使用 puts() 显示字符串时，系统会自动在其后添加一个换行符,而使用printf需要换行符 '\n' 
* 输出str，直到遇到“x00”字符为止。也就是说，puts函数输出的数据长度是不受控的，只要我们输出的信息中包含x00截断符，输出就会终止，且会自动将“n”追加到输出字符串的末尾
* 返回：如果成功，该函数返回一个非负值为字符串长度（包括末尾的 **\0**），如果发生错误则返回 EOF

