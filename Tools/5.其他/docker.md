# docker

## 1.基础

docker常用命令：

- `docker pull ubuntu:latest`：拉取指定版本镜像，换源`docker pull docker.1ms.run/ubuntu:latest`
- `docker run -itd -p 8000:80 --name ubuntu-test ubuntu`：创建并启动ubuntu容器
  - `-i`：交互式操作
  - `-t`：终端
  - `-d`：后台运行
  - `-p`:端口映射，容器80映射到主机8000
  - `--name`：指定容器名称

- `docker ps`:  列出所有正在运行的容器，包括每个容器的ID。容器id是每个容器的唯一字母数字
- `docker ps -a`：列出所有容器，无论它们是否正在运行。
- `docker exec -it <container id> /bin/bash`：在运行容器中执行`/bin/bash`命令。我们将得到一个shell提示符。不需要键入整个ID字符串;键入前几个字符就足够了，只要它们是唯一的
- `docker rm <container id>`：移除容器。


很多时候，我们需要在容器和主机之间传输文件。这可以很容易地使用`docker cp`命令完成。请参阅以下示例。

```
$ docker ps
CONTAINER ID        NAMES       ...
bcff498d0b1f     host-10.9.0.6  ...
1e122cd314c7     host-10.9.0.5  ...
31bd91496f62     host-10.9.0.7  ...

// From host to container
$ docker cp  file.txt  bcff:/tmp/
$ docker cp  folder  bcff:/tmp

// From container to host 
$ docker cp  bcff:/tmp/file.txt .
$ docker cp  bcff:/tmp/folder  .
```



## 2.dockerfile

Docker可以通过从`Dockerfile`中阅读指令来**自动构建镜像**，`Dockerfile`是一个文本文件，包含构建容器镜像所需的所有命令

可以修改from后的ubuntu:20.04，换成带镜像的，目前使用的镜像https://docker.xuanyuan.me/，cdn加速毫秒镜像：https://1ms.run/

```dockerfile
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# Install software packages inside the container
RUN apt-get update  \
    && apt-get -y install  \
          iputils-ping \
          iproute2  \
          net-tools \
          dnsutils  \
          mtr-tiny  \
          nano      \
    && apt-get clean

# Put file inside the container
COPY file  /

# The command executed by the container after startup
CMD [ "/bin/bash"]
```

上面的`Dockerfile`表示我们的容器是在官方Ubuntu 20.04 Docker镜像之上构建的。这就是`FROM`命令的目的。在这个基础映像之上，我们使用`RUN`命令安装一些附加软件包，包括一些网络实用程序和`nano`编辑器。最后的`"apt-get clean"`命令会清除`/var/cache`中保留的已检索包文件的本地存储库，因此可以减小最终映像的大小



构建镜像：`docker build -t nginx:v3 .`

- -t 参数用于指定镜像名称和标签
- 最后的 . 表示构建上下文路径，构建镜像时使用的文件路径



## 3.docker-compose

使用 docker-compose.yml 定义运行多容器服务