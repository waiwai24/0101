## 1.cmd与power shell

cmd 是 power shell的子集



## 2. 说明

* 不区分大小写
* 上下键可查看历史命令
* tab键可自动补全
* 获取帮助命令 `/？`



## 3.常用命令

1. echo显示输出 pause暂停 cls清屏 exit退出

2. 进入磁盘

```cmd
D: #进入d盘
F: #进入F盘
```

3. cd命令

```cmd
cd /? #获取使用帮助
cd \ #跳转到硬盘的根目录
cd C:\WINDOWS #跳转到当前硬盘的其他文件
d: #跳转到其他硬盘
cd /d e:\software #跳转到其他硬盘的其他文件夹，注意此处必须加/d参数。否则无法跳转
cd.. #跳转到上一层目录
```

4. 创建/删除目录

```cmd
md 目录名（文件夹）#创建目录
rd 目录名（文件夹）#删除目录
```

5. 删除文件

```cmd
del 文件名 #这个是专门删除文件的，不能删除文件夹
```

6. 查看文件内容

```cmd
type 文件名
```

7. 查看目录所有内容

```cmd
dir #类似于Linux下的ls
tree
```

8. IP信息

```cmd
ipconfig
ipconfig /all
```

9. mac地址

```cmd
getmac /v
```

10. 网络连接测试ping

11. copy

```cmd
copy /b a.xxx [+b.xxx [+...]] c.xxx #[]代表可选意思是将a.xxx和b.xxx合并为c.xxx。
```

