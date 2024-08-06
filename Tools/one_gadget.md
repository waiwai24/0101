# one_gadget

```shell
$ one_gadget libc-2.23.so

0x45226 execve("/bin/sh", rsp+0x30, environ)
constraints:
  rax == NULL                                # 这个提示的意思就是在调用one_gadget前需要满足的条件

0x4527a execve("/bin/sh", rsp+0x30, environ)
constraints:
  [rsp+0x30] == NULL

0xf03a4 execve("/bin/sh", rsp+0x50, environ)
constraints:
  [rsp+0x50] == NULL
```



* one_gadget是libc中存在的一些执行`execve("/bin/sh", NULL, NULL)`的片段，当可以泄露libc地址，并且可以知道libc版本的时候，可以使用此方法来快速控制指令寄存器开启shell。

* 相比于`system("/bin/sh")`，这种方式更加方便，不用控制RDI、RSI、RDX等参数。运用于不利构造参数的情况
* **注意**：one_gadget并不总是可以获取shell，它首先要满足一些条件才能执行成功

