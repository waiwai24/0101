# Vul、Poc、Exp、Payload、Shellcode



## 1.Vul

Vulnerability 漏洞

## 2.Poc

Proof of Concept概念验证/观点证明，这个短语会在漏洞报告中使用，漏洞报告中的POC则是一段说明或者一个攻击的样例，使得读者能够确认这个漏洞是真实存在的常指一段漏洞整明的代码

## 3.Exp

Exploit  漏洞利用，意思是一段对漏洞如何利用的详细说明或者一个演示的漏洞攻击代码，可以使得读者完全了解漏洞的机理以及利用的方法，指利用系统漏洞进行攻击的动作

## 4.Payload

有效载荷，指成功Exp后，真正在目标系统执行的代码或指令

## 5.Shellcode

shell代码，是Payload的一种，由于其建立正向/反向shell而得名。

 

## 6.段子记忆法

你在监控某人，突然觉得他家的窗户可能没关好，这可能是一个Vul，你去推了推，发现推开了，那这就是一个Poc，你验证了这个漏洞。第二天你实施了计划，推窗进去了。查看了机密文件，安装了窃听器，那这做的就是一个Exp，在他家所做的就是不同的Payload，窃听器就是一个shellcode

  

## 7.其他

- cve---Common Vulnerabilities & Exposures 共漏洞和暴露，漏洞编号，漏洞字典，国际上的
- cnvd---漏洞编号，漏洞字典，咱们自己的
- 0day---没打补丁，没公开的漏洞
- apt---Advanced Persistent Threat 高级可持续性攻击
- Pwn--是一个黑客语法的俚语词 ，是指攻破设备或者系统