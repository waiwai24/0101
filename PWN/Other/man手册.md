由于系统命令可能会和库函数重叠，所以可以指定num去查看对应的手册

```shell
   1   Executable programs or shell commands
   2   System calls (functions provided by the kernel)
   3   Library calls (functions within program libraries)
   4   Special files (usually found in /dev)
   5   File formats and conventions, e.g. /etc/passwd
   6   Games
   7   Miscellaneous (including macro packages and conventions), e.g. man(7), groff(7), man-pages(7)
   8   System administration commands (usually only for root)
   9   Kernel routines [Non standard]
```



安装基本文档：

```shell
sudo apt-get install libc-dev
sudo apt-get install glibc-doc
sudo apt-get install manpages
sudo apt-get install manpages-de
sudo apt-get install manpages-de-dev
sudo apt-get install manpages-dev

sudo apt-get install manpages-posix
sudo apt-get install manpages-posix-dev

sudo apt-get install linux-doc
sudo apt-get install libcorelinux-dev

sudo apt-get install libstdc++-7-dev
sudo apt-get install libstdc++-7-doc

sudo apt-get install manpages*
```

