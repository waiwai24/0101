# Make

Makefile文件由一系列规则组成，每条规则形式如下：

```
<target> : <prerequisites> 
[tab]  <commands>
```

冒号前面的部分，叫做"目标"（target），冒号后面的部分叫做"前置条件"（prerequisites）；第二行必须由一个tab键起首，后面跟着"命令"（commands）。

"目标"是必需的，不可省略；"前置条件"和"命令"都是可选的，但是两者之中必须至少存在一个。

每条规则就明确两件事：构建目标的前置条件是什么，以及如何构建。下面就详细讲解，每条规则的这三个组成部分

* target：

  * 通常是文件名，指明Make命令所要构建的对象，目标可以是一个文件名，也可以是多个文件名，之间用空格分隔。

  * 除了文件名，目标还可以是某个操作的名字，这称为"伪目标"（phony target）

    ```
    Makefile：
    clean:
          rm *.o
          
    $ make  clean
    
    但是，如果当前目录中，正好有一个文件叫做clean，那么这个命令不会执行。因为Make发现clean文件已经存在，就认为没有必要重新构建了，就不会执行指定的rm命令，为了避免这种情况，可以明确声明clean是"伪目标"
    .PHONY: clean
    clean:
            rm *.o temp
    ```

  * 如果Make命令运行时没有指定目标，默认会执行Makefile文件的第一个目标。


        $ make