# gcc与g++



## 1.背景知识

GCC:GNU Compiler Collection(GUN 编译器集合)，它可以编译C、C++、JAV、Fortran、Pascal、Object-C等语言。

gcc是GCC中的GUN C Compiler（C 编译器）

g++是GCC中的GUN C++ Compiler（C++编译器）



## 2.程序处理流程

![image-20240303234108791](./assets/gcc与g++/image-20240303234108791.png)

- **预处理**： 编译器处理预处理命令，包括头文件包含、宏定义的扩展、条件编译的选择等；
- **编译**：将预处理后的源代码文件 *翻译转换* 得到机器语言的目标程序，得到机器语言**汇编文件**；
- **汇编**：将汇编代码翻译成**机器码**，此时的机器码尚不能直接运行；
- **链接**：处理可重定位文件，把各种符号引用和符号定义转换成为可执行文件中的合适信息，通常是虚拟地址。



## 3.常用命令

```shell
gcc [options] [filenames]
gcc -E hello.c -o hello.i
gcc -S hello.i -o hello.s
gcc -c hello.s -o hello.o
gcc hello.o -o hello.exe
gcc hello.c -o hello -save-temps  
```

常用参数：

- `-E`：对文件作预处理，将`#`开始的预处理指令转换后直接插入到程序文本中
- `-S`：对文件进行编译
  - Linux下的gdb和gcc默认输出的汇编都是AT&T格式的但是它们都有方式来转换为Intel格式。
  - -masm=[intel|att] 选择intel或AT&T的汇编语法，AT&T和Intel格式中的源操作数和目标操作数的位置正好相反
  - 参考：https://zhuanlan.zhihu.com/p/527208939

- `-c`：对文件进行汇编
- `-o`：指定输出文件名
- `-g`：保留调试信息，通常用gdb分析时要使用此参数
- `-O0`:不进行优化处理
- `-O 或 -O`：优化生成代码
- `-O2`：进一步优化。
- `-O3`：比 -O2 更进一步优化，包括 inline 函数。
- `-save-temps` ： Do not delete intermediate files.
- `m32`：编译32位程序命令
- `-static`：静态链接
- `-fno-stack-protector` 



## 4.gcc与g++的区别

1. 对于 *.c和*.cpp文件，gcc分别当做c和cpp文件编译（c和cpp的语法强度是不一样的）
2. 对于 *.c和*.cpp文件，g++则统一当做cpp文件编译
3. 使用g++编译文件时，**g++会自动链接标准库STL，而gcc不会自动链接STL**
4. gcc在编译C文件时，可使用的预定义宏是比较少的
5. gcc在编译cpp文件时/g++在编译c文件和cpp文件时（这时候gcc和g++调用的都是cpp文件的编译器），会加入一些额外的宏。

6. 在用gcc编译c++文件时，为了能够使用STL，需要加参数 –lstdc++ ，但这并不代表 gcc –lstdc++ 和 g++等价，它们的区别不仅仅是这个
