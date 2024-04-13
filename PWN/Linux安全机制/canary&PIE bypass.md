canary



canary是用来保护用来**防护栈溢出**的保护机制

原理：在函数入口处放入一个值存到栈上，当函数结束运行时会检查这个栈上的值和存进去的值是否一致

bypass：

* 格式化字符串绕过canary
* canary爆破
* stack smashing
* 劫持_stack_chk_fail







PIE技术是一个针对