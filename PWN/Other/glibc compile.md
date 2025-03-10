

# glibc compile

* 源码下载：

  * https://launchpad.net/ubuntu/+source/glibc （推荐该网站的源码，和下面gnu给的源码安装配置中有些许不同，适配ubuntu，基本不会出现一些报错的情况）
  * http://ftp.gnu.org/gnu/glibc/

* tar解压，并进入目录

* ```shell
  mkdir build;cd build
  
  64位：
  ../configure --prefix=/path_you_want  --disable-werror --enable-debug=yes
  32位：
  ../configure --prefix=/path_you_want --disable-werror --enable-debug=yes --host=i686-linux-gnu --build=i686-linux-gnu CC="gcc -m32" CXX="g++ -m32" 
  
  make -j16
  make install DESTDIR=/xxx/xxx/install
  ```



glibc2.39 编译遇到的问题：

```shell
syslog.c: In function ‘__vsyslog_internal’:
syslog.c:95:30: error: inlining failed in call to ‘always_inline’ ‘syslog’: function not inlinable
   95 | ldbl_strong_alias (__syslog, syslog)
      |                              ^~~~~~
./../include/libc-symbols.h:143:26: note: in definition of macro ‘_strong_alias’
  143 |   extern __typeof (name) aliasname __attribute__ ((alias (#name))) \
      |                          ^~~~~~~~~
../sysdeps/generic/math_ldbl_opt.h:14:44: note: in expansion of macro ‘strong_alias’
   14 | #define ldbl_strong_alias(name, aliasname) strong_alias (name, aliasname)
      |                                            ^~~~~~~~~~~~
syslog.c:95:1: note: in expansion of macro ‘ldbl_strong_alias’
   95 | ldbl_strong_alias (__syslog, syslog)
      | ^~~~~~~~~~~~~~~~~
syslog.c:138:7: note: called from here
  138 |       syslog (INTERNALLOG, "syslog: unknown facility/priority: %x", pri);
      |       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
      
make[2]: *** [../o-iterator.mk:9：/glibc/glibc_2.39.orig/glibc-2.39/build/misc/syslog.o] 错误 1
make[2]: *** 正在等待未完成的任务....
make[2]: 离开目录“/glibc/glibc_2.39.orig/glibc-2.39/misc”
make[1]: *** [Makefile:484：misc/subdir_lib] 错误 2
make[1]: 离开目录“/glibc/glibc_2.39.orig/glibc-2.39”
make: *** [Makefile:9：all] 错误 2

```

解决：对syslog.c的138行注释：

```shell
//syslog (INTERNALLOG, "syslog: unknown facility/priority: %x", pri);
```



遇到的问题：

```shell
collect2: error: ld returned 1 exit status
```

解决：修改configure配置文件，7474行修改为：

```shell
no_fortify_source="-U_FORTIFY_SOURCE"
```

