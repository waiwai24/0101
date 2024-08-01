# PIE

PIE（Position Independent Executable）需要配合 ASLR  来使用，以达到可执行文件的加载时地址随机化。简单来说，PIE 是编译时随机化，由编译器完成；ASLR 是加载时随机化，由操作系统完成。ASLR  将程序运行时的堆栈以及共享库的加载地址随机化，而 PIE 在编译时将程序编译为位置无关、即程序运行时各个段加载的虚拟地址在装载时确定。开启  PIE 时，编译生成的是动态库文件（Shared object）文件，而关闭 PIE 后生成可执行文件（Executable）
