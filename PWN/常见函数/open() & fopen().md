# open() & fopen()

## 1.open()

```c
int open(const char * filename, int flags);
int open(const char * filename, int flags, mode_t mode);
```

* 头文件

  ```c
  #include <sys/types.h>    
  #include <sys/stat.h>    
  #include <fcntl.h>
  ```

* 返回值：若所有欲核查的权限都通过了检查则返回0 值, 表示成功, 只要有一个权限被禁止则返回-1

* flags：

  | O_RDONLY    | 以只读方式打开文件                                           |
  | ----------- | ------------------------------------------------------------ |
  | O_WRONLY    | 以只写方式打开文件                                           |
  | O_RDWR      | 以可读写方式打开文件. 上述三种旗标是互斥的, 也就是不可同时使用, 但可与下列的旗标利用OR( |
  | O_CREAT     | 若欲打开的文件不存在则自动建立该文件.                        |
  | O_EXCL      | 如果O_CREAT 也被设置, 此指令会去检查文件是否存在. 文件若不存在则建立该文件, 否则将导致打开文件错误. 此外, 若O_CREAT |
  | O_NOCTTY    | 如果欲打开的文件为终端机设备时, 则不会将该终端机当成进程控制终端机. |
  | O_TRUNC     | 若文件存在并且以可写的方式打开时, 此旗标会令文件长度清为0, 而原来存于该文件的资料也会消失. |
  | O_APPEND    | 当读写文件时会从文件尾开始移动, 也就是所写入的数据会以附加的方式加入到文件后面. |
  | O_NONBLOCK  | 以不可阻断的方式打开文件, 也就是无论有无数据读取或等待, 都会立即返回进程之中. |
  | O_NDELAY    | 同**O_NONBLOCK.**                                            |
  | O_SYNC      | 以同步的方式打开文件.                                        |
  | O_NOFOLLOW  | 如果参数pathname 所指的文件为一符号连接, 则会令打开文件失败. |
  | O_DIRECTORY | 如果参数pathname 所指的文件并非为一目录, 则会令打开文件失败。 |

* 参数mode则有下列数种组合, 只有在建立新文件时才会生效, 此外真正建文件时的权限会受到umask 值所影响, 因此该文件权限应该为 (mode-umaks).

  | mode             | 权限                                                      |
  | ---------------- | --------------------------------------------------------- |
  | **S_IRWXU00700** | 权限, 代表该文件所有者具有可读、可写及可执行的权限.       |
  | **S_IRUSR**      | 或S_IREAD, 00400 权限, 代表该文件所有者具有可读取的权限.  |
  | **S_IWUSR**      | 或S_IWRITE, 00200 权限, 代表该文件所有者具有可写入的权限. |
  | **S_IXUSR**      | 或S_IEXEC, 00100 权限, 代表该文件所有者具有可执行的权限.  |
  | **S_IRWXG**      | 00070 权限, 代表该文件用户组具有可读、可写及可执行的权限. |
  | **S_IRGRP**      | 00040 权限, 代表该文件用户组具有可读的权限.               |
  | **S_IWGRP**      | 00020 权限, 代表该文件用户组具有可写入的权限.             |
  | **S_IXGRP**      | 00010 权限, 代表该文件用户组具有可执行的权限.             |
  | **S_IRWXO**      | 00007 权限, 代表其他用户具有可读、可写及可执行的权限.     |
  | **S_IROTH**      | 00004 权限, 代表其他用户具有可读的权限                    |
  | **S_IWOTH**      | 00002 权限, 代表其他用户具有可写入的权限.                 |
  | **S_IXOTH**      | 00001 权限, 代表其他用户具有可执行的权限…                 |



## 2.fopen()

```c
FILE *fopen(const char *filename, const char *mode)
```

* 头文件 : #include<stdio.h>

* 函数返回一个 FILE 指针。否则返回 NULL，且设置全局变量 errno 来标识错误

* filename -- 字符串，表示要打开的文件名称。

* mode -- 字符串，表示文件的访问模式，可以是以下表格中的值：

| 模式 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| "r"  | 打开一个用于读取的文件。该文件必须存在。                     |
| "w"  | 创建一个用于写入的空文件。如果文件名称与已存在的文件相同，则会删除已有文件的内容，文件被视为一个新的空文件。 |
| "a"  | 追加到一个文件。写操作向文件末尾追加数据。如果文件不存在，则创建文件。 |
| "r+" | 打开一个用于更新的文件，可读取也可写入。该文件必须存在。     |
| "w+" | 创建一个用于读写的空文件。                                   |
| "a+" | 打开一个用于读取和追加的文件。                               |

