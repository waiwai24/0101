# pwntools

```python
from pwm import *
```

注意：py3使用时确保所有字符串都有个`b`前缀



## 1.tubes

* `interactive()`：同时读写管道，相当于回到 shell 模式进行交互，在取得 shell 之后调用
* `recv(num,timeout=default)`：接收指定数量的可用字节
* `recvall()`：接受数据直到EOF
* `recvline()`：接受一行数据
* `recvuntil(delims, timeout=default)`：接收数据直到 delims 出现
* `send(data)`：发送数据
* `sendline(data)`：发送一行数据，默认在行尾加\n
* `close()`：关闭管道

主要的子模块：

* 进程`p=process("/bin/sh")`
* 套接字`r=remote('1270.0.1',1080)`,`l=listen(1080)`
* SSH `s=ssh(host='example.com',user='name',password='passwd')`



## 2.pack&unpack

打包/解包任意长度的整数，默认小端

* `p16()`，`p32()`：打包16/32位的整数
* `u16()`，`u32()`：解包16/32位的整数



## 3.哈希和编码

* `b64e()`，`b64d()`
* `md5sumhex()`，`md5filehex()`，
* `sha1sumhex()`
* `enhex`,`unhex`
* 