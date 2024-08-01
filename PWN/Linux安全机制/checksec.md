# checksec



## 1.简介

checksec 可以识别编译时构建到二进制文件中的安全属性，是一个单文件的 shell 脚本，它位于 `/usr/bin/checksec`



各种安全技术的编译参数如下：

| 安全技术 | 完全开启              | 部分开启          | 关闭                 |
| -------- | --------------------- | ----------------- | -------------------- |
| Canary   | -fstack-protector-all | -fstack-protector | -fno-stack-protector |
| NX       | -z noexecstack        |                   | -z execstack         |
| PIE      | -pie                  |                   | -no-pie              |
| RELRO    | -z now                | -z lazy           | -z norelro           |