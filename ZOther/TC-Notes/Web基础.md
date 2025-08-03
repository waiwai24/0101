# Web基础



## 1.web通信

### 1.1 url协议

### 1.2 http协议



## 2.web前端基础

### 2.1 html

常见标签：

* 注释：<!--  内容  -->

* 图像：<img src ='’“alt=”“>

* 链接：<a href=" "></a>

* 表单：<form action="post"></form>

  

### 2.2 JavaScript

世界最流行的脚本语言



## 3.常见web漏洞

### 3.1 暴力破解

自动化工具/脚本穷举

### 3.2. xss跨站脚本攻击

篡改网页，插入恶意脚本，盗取用户信息，钓鱼

* 反射：携带xss脚本的链接
* 存储：存储在服务器
* dom

### 3.3 csrf跨站请求伪造

利用已登录的身份，以用户名义完成非法操作，执行恶意操作，制造蠕虫

### 3.4 sql注入

未对用户输入数据的合法性没用进行过滤或者判断

### 3.5 rce远程代码执行

普通dos命令：ipconfig，dir，echo，net user

web应用进行命令注入：

* php：system，exec，shell_exec，eval
* python：os.system()
* java：runtime.getruntime.exec()
* 函数或函数参数可控

### 3.6 文件操作漏洞（文件上传，读取，写入）

* 上传头像，附件
* 下载系统任意文件，程序代码
* 上传webshell，马



## 4.常见web安全工具

### 4.1 常见游览器扩展

* xdebug
* foxyproxy
* wappalyzer

### 4.2 代理抓包工具

### 4.3 扫描和其他在线工具