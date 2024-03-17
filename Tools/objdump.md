# objdump



## 1.简介

objdump命令来自于英文词组“object files dump”（dump转储）的缩写，其功能是用于**显示**目标文件附加信息，以一种可阅读的格式让你更多地了解二进制文件可能带有的附加信息




## 2.使用

```shell
objdump <option(s)> <file(s)>
```

常用参数:

* `-h`：Display the contents of the section headers
* `-x`：Display the contents of all headers

* `-s`：显示指定section的完整内容。默认所有的非空section都会被显示
* `-d`：从objfile中反汇编那些特定指令机器码的section
* `-M intel`： 选择intel语法模式

