# RELRO

## 1.原理

RELRO（ReLocation Read-Only）设置符号重定向表为只读或在程序启动时就解析并绑定所有动态符号，从而减少对 GOT（Global Offset Table）的攻击。

RELOR 有3种形式：

- No RELRO：关闭RELRO
- Partial RELRO：gcc默认的relro等级，一些段（包括 `.dynamic`）在初始化后将会被标记为只读。没有开启 RELRO 保护的前提下，每个 libc 的函数对应的 GOT 表项是可以被修改的
- Full RELRO：除了 Partial RELRO，延迟绑定将被禁止，所有的导入符号将在开始时被解析，`.got.plt` 段会被完全初始化为目标函数的最终地址，并被标记为只读不可写（无法修改got表）。另外 `link_map` 和 `_dl_runtime_resolve` 的地址也不会被装入

