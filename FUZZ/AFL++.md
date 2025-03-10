# AFL++

> AFL++ 是 Google AFL 的一个优秀分支 - 速度更快、突变更多更好、仪器更多更好、支持自定义模块等
>
> AFL++ 与 AFL 都是灰盒 fuzzer，但不能用于纯黑盒（out of the box） fuzz

## 1.基本原理

为了让AFL工作，需要使用特殊的AFL编译器编译二进制文件（插桩，记录代码覆盖率）

AFL++编译器的选择：

```text
+--------------------------------+
| clang/clang++ 11+ is available | --> use LTO mode (afl-clang-lto/afl-clang-lto++)
+--------------------------------+     see [instrumentation/README.lto.md](instrumentation/README.lto.md)
    |
    | if not, or if the target fails with LTO afl-clang-lto/++
    |
    v
+---------------------------------+
| clang/clang++ 3.8+ is available | --> use LLVM mode (afl-clang-fast/afl-clang-fast++)
+---------------------------------+     see [instrumentation/README.llvm.md](instrumentation/README.llvm.md)
    |
    | if not, or if the target fails with LLVM afl-clang-fast/++
    |
    v
 +--------------------------------+
 | gcc 5+ is available            | -> use GCC_PLUGIN mode (afl-gcc-fast/afl-g++-fast)
 +--------------------------------+    see [instrumentation/README.gcc_plugin.md](instrumentation/README.gcc_plugin.md) and
                                       [instrumentation/README.instrument_list.md](instrumentation/README.instrument_list.md)
    |
    | if not, or if you do not have a gcc with plugin support
    |
    v
   GAME OVER! Install gcc-VERSION-plugin-dev or llvm-VERSION-dev
```



```shell
afl-fuzz -i [input] -o [output] [options] -- /path/to/fuzzed/binary [@@]

-i：输入的测试用例目录
-o：输出fuzz结果的目录
-s：
```



## 2.安装

https://github.com/AFLplusplus/AFLplusplus

推荐本地编译，不推荐docker容器（性能受损）



## 3.深度fuzz

指的是在有源码的情况下

模糊测试源代码分为三个步骤：

- 使用专门的编译器编译目标，以便有效地对目标进行模糊测试。此步骤称为“对目标进行检测”
- 通过选择和优化目标的输入语料库来准备模糊测试
- 通过随机改变输入并评估该输入是否在目标二进制中的新路径上进行处理来执行目标的模糊测试

