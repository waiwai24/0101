# readlef



## 1.简介

用于显示 `elf` 格式文件的信息，与`objdump`类似，但是它显示的信息更为具体



## 2.使用

```shell
readelf <option(s)> elf-file(s)
```

常用参数:

* `-a` ,  `--all`:  显示全部信息
* `-h` ,  `--file-header` ：显示 `elf` 文件开始的文件头信息

* `-l` ,  `--program-headers` ,  `--segments`：  显示程序头（段头）信息(如果有的话)
* `-S` ,  `--section-headers` ,  `--sections`  ：显示节头信息(如果有的话)

* `-e `，`--headers`： 显示全部头信息，等价于: -h -l -S 
