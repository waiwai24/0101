# sprintf() & __snprintf_chk()

```c
int sprintf(char *str, const char *format, ...)
```

* 发送格式化输出到 **str** 所指向的字符串
* **str** -- 这是指向一个字符数组的指针，该数组存储了 C 字符串
* **format** -- 这是字符串，包含了要被写入到字符串 str 的文本



```c
int __snprintf_chk(char *str, size_t size, int flag, size_t ssiz, const char *format, ...);
```

* str：指向要写入格式化输出的缓冲区的指针
* size：指定缓冲区str的大小
* flag：标志位，启用额外的检查
  * `0`：不启用额外检查
  * `1`：启用基本检查
  * `2`：启用更严格的检查
* ssiz：再次指定缓冲区的大小，用于安全检查
* format：格式化字符串
* ...：可变参数列表