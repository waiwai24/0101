# tmux



## 1.功能

- 它允许在单个窗口中，同时访问多个会话。这对于同时运行多个命令行程序很有用。
- 它可以让新窗口"接入"已经存在的会话。
- 它允许每个会话有多个连接窗口，因此可以多人实时共享会话。
- 它还支持窗口任意的垂直和水平拆分。



## 2.基本用法

* `tmux`：启动tmux
* `ctrl+d`,`exit`：退出tmux
* `tmux new -s <session-name>`：新建会话
* `tmux rename-session`：重命名会话
* `tmux detach`：分离会话，但会话和里面的进程仍在后台运行
* `tmux ls`：查看所有会话
* `tmux attach`：接入会话
  * 使用会话编号`tmux attach -t 0`
  * 使用会话名称`tmux attach -t <session-name>`
* `tmux kill-session -t`：杀死会话
* `tmux switch -t`：切换会话



## 3.快捷键

都是`ctrl+b+快捷键`

* %：分成左右两个窗口
* ”：分成上下两个窗口
* o：光标切换到下一个窗口
* {：左移当前窗口
* }：右移当前窗口
* space：切换窗口布局