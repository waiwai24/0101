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

asan:buffer overflow,uaf

ubsan

datafolwsanitizer