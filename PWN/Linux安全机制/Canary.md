# Canary



## 1.背景

栈溢出保护是一种缓冲区溢出攻击缓解手段，当函数存在缓冲区溢出攻击漏洞时，攻击者可以覆盖栈上的返回地址来让shellcode能够得到执行



## 2.原理

canary是用来保护用来**防护栈溢出**的保护机制，插在局部变量和保存的上一个rbp中间

函数开始执行的时候会先往栈里插入cookie信息，当函数真正返回的时候会验证cookie信息是否合法，如果不合法就停止程序运行。攻击者在覆盖返回地址的时候往往也会将cookie信息给覆盖掉，导致栈保护检查失败而阻止shellcode的执行。在Linux中我们将cookie信息称为canary。

```
.text:0000000000001189 endbr64
.text:000000000000118D push rbp
.text:000000000000118E mov rbp, rsp
.text:0000000000001191 sub rsp, 30h
.text:0000000000001195 mov rax, fs:28h //插入canary
.text:000000000000119E mov [rbp-8], rax
...
.text:00000000000011CE mov rdx, [rbp-8]
.text:00000000000011D2 xor rdx, fs:28h //异或，同为0，异为1
.text:00000000000011DB jz short locret_11E2
.text:00000000000011DB
.text:00000000000011DD call ___stack_chk_fail
.text:00000000000011DD
.text:00000000000011E2 ; --------------------------------------------------------
-------------------
.text:00000000000011E2
.text:00000000000011E2 locret_11E2: ; CODE XREF:
f+52↑j
.text:00000000000011E2 leave
```



## 3.开启方式

```shell
gcc -o test test.c						
// 默认情况下，不开启Canary保护
gcc -fno-stack-protector -o test test.c  
//禁用栈保护
gcc -fstack-protector -o test test.c   
//启用堆栈保护，不过只为局部变量中含有 char 数组的函数插入保护代码
gcc -fstack-protector-all -o test test.c 
//启用堆栈保护，为所有函数插入保护代码
```

开启 CANARY 的时候，提示检测到栈溢出和段错误，而关闭的时候，只有提示段错误

## 4.bypass

* 格式化字符串绕过canary
* canary爆破
* stack smashing
* 劫持_stack_chk_fail







