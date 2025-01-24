# strlen()

```c
size_t strlen(const char *str)
```

* 计算字符串 **str** 的长度，直到空结束字符，但不包括空结束字符
* 利用：利用strlen函数判断字符串时以 **b’\x00’** 结尾，可以用b’\x00’绕过strlen的判断
