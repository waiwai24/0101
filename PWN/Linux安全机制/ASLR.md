# ASLR

Address Space Layout Randomization

ASLR 是系统级别的地址随机。通过修改 /proc/sys/kernel/randomize_va_space 的值可以控制ASLR 的级别

由于程序的堆、栈分配与共享库的装载都是在运行时进行, 系统在程序每次执行时, 随机地分配程序堆栈的地址以及共享库装载的地址。尽管它们之间的相对位置没有改变, 但每次执行的差异仍然是页级的, 攻击者将无法预测自己写入的数据区的确切虚拟地址

```
下面命令都可以查看保护级别：
sysctl -a --pattern randomize
cat /proc/sys/kernel/randomize_va_space
关闭aslr：
sudo echo 0 > /proc/sys/kernel/randomize_va_space
```

* 0：关闭 ASLR
* 1：栈基址，共享库，mmap 基址随机
* 2：在 1 的基础上增加堆基址的随机

关闭 PIE:

* 关闭 ASLR： 主模块加载地址固定（0x400000），所有模块加载地址固定
* 开启 ASLR：主模块加载地址固定（0x400000），其他模块加载地址不固定

开启 PIE:

* 关闭 ASLR：所有模块加载地址固定，主模块地址（主模块基址 0x55xxxxxxxxxx且固定)
* 开启 ASLR：所有模块加载地址不固定