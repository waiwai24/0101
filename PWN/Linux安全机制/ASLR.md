# ASLR

## 1.原理

ASLR 是系统级别的地址随机。通过修改 /proc/sys/kernel/randomize_va_space 的值可以控制ASLR 的级别：

* 0：关闭 ASLR
* 1：栈基址，共享库，mmap 基址随机
* 2：在 1 的基础上增加堆基址的随机

关闭 PIE
关闭 ASLR： 主模块加载地址固定（0x400000），所有模块加载地址固定
开启 ASLR：主模块加载地址固定（0x400000），其他模块加载地址不固定

开启 PIE
关闭 ASLR：所有模块加载地址固定，主模块地址（主模块基址 0x55xxxxxxxxxx且固定)
开启 ASLR：所有模块加载地址不固定