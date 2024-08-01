# read()函数

```c
ssize_t read(int fd, void *buf, size_t count)
```

* 读取打开文件的count字节保存到buf缓冲区，返回实际读取的字节数
* fd=0，代表标准输入流；File Descriptor (FD)：stdin = 0、stdout = 1和stderr = 2