# __readfsbyte、__readfsdword、__readfsqword、__readfsword

```C
unsigned char __readfsbyte(
   unsigned long Offset
);
unsigned short __readfsword(
   unsigned long Offset
);
unsigned long __readfsdword(
   unsigned long Offset
);
unsigned __int64 __readfsqword(
   unsigned long Offset
);
```

* 从相对于 FS 段开头的偏移量指定的位置读取内存
* 参数*Offset* [in] 从 `FS` 的开头开始读取的偏移量
* 返回值位置 `FS:[Offset]` 处的字节、字、双字或四字（由调用的函数名称指示）的内存内容