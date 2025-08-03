# system奇技淫巧

就system的参数而言，以下三种参数，都可以返回shell：

* `/bin/sh`

* `sh`

* `$0`：

  * 会使用与运行脚本相同的shell环境来执行命令，本地shell的环境变量：

    ![](./assets/system奇技淫巧/image-20250402111240482.png)

  * 十六进制为0x2430，有时候可以在题目文件中搜索一下

