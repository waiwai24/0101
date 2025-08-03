# rename()

```c
#include <stdio.h>

int rename(const char *oldpath, const char *newpath);

#include <fcntl.h>           /* Definition of AT_* constants */
#include <stdio.h>

int renameat(int olddirfd, const char *oldpath,
             int newdirfd, const char *newpath);

int renameat2(int olddirfd, const char *oldpath,
              int newdirfd, const char *newpath, unsigned int flags);

# namedat2()：
# _GNU_SOURCE
```

* rename():
  * 将文件名从 *oldpath* 指向的名称更改为 *newpath* 指向的名称，两者必须具有相同类型，即两个目录或两个文件，但依赖全局路径
  * 如果 *newpath* 已存在，那么在将 *oldpath* 重命名为 *newnpath* 之前将其除去。 因此，如果 *newpath* 指定现有目录的名称，那么它必须是空目录
  * 成功返回 0，不成功返回非 0
* renameat()：
  *  多了目录文件描述符，支持相对路径和特定目录的 FD
  * 成功返回 0，不成功返回非 0
* renameat2():
  * 与 renameat()相比， renameat2() 具有额外的 flags 自变量。 不带 flags 参数的 renameat2() 调用等同于 renameat()
  * 如果 flags 包含 RENAME_EXCHANGE，则不会删除位于 newname 的现有文件，相反，它将被重命名为 oldname。因此，有了这个标志，可以使用 renameat2()原子地交换两个文件
  * 成功返回 0，不成功返回 -1