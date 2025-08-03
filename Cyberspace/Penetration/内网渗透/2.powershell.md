# powershell



## 1.介绍

* PowerShell 可以简单的理解为 cmd 的高级版，cmd 能做的事在 PowerShell 中都能做，但 PowerShell 还能做很多 cmd 不能做的事情
* ps1 是PowerShell 的脚本扩展名，一个 PowerShell 脚本文件其实就是一个简单的文本文件
* 脚本执行策略（为了防止恶意脚本在 PowerShell 中被运行，PowerShell 有个执行策略，默认情况下，这个执行策略是受限模式`Restricted`）
  * 查看当前执行策略`Get-ExecutionPolicy`
  * **Restricted**：不能运行脚本
  * **RemoteSigned**：本地创建的脚本可以运行，但从网上下载的脚本不能运行（除非它们拥有由受信任的发布者签署的数字签名)
  * **AllSigned**：仅当脚本由受信任的发布者签名才能运行
  * **Unrestricted**：脚本执行不受限制，不管来自哪里，也不管它们是否有签名
  * 使用`Set-ExecutionPolicy <policy name>`设置执行策略，该命令需要管理员权限



## 2.脚本执行

* 绕过本地权限：加上 `-ExecutionPolicy Bypass`
* 绕过本地权限并隐藏执行，加入`-WindowStyle Hidden -NoLogo -NonInteractive -NoProfile`