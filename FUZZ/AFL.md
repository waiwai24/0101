coverage and evolve：

* basic block（单入单出）
* hash id for blocks and edges
* store hit count：bitmap
  * trace_bits：单个
  * virgin_bits：全局
  * testcase（whether good）：compare these two type bits



trace coverage：

* idea1：monitor application‘s execution，tool：PIN（only base on intel）hardware
* idea2：instruction pin



mdoe：

* llvm（src）
* gcc（src）
* qemu（binary only）



has_new_bits



security violation：

asan:buffer overflow, uaf

ubsan

datafolwsanitizer



源码编译程序时进行插桩，以记录代码覆盖率（Code Coverage）

初始测试集加入输入队列（queue）；

将队列中的文件按一定的策略进行“突变”；

如果经过变异文件更新了覆盖范围，则将其保留添加到队列中;

上述过程会一直循环进行，期间触发了crash的文件会被记录下来