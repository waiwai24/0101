# docker

Docker可以通过从`Dockerfile`中阅读指令来自动构建镜像，`Dockerfile`是一个文本文件，包含构建容器镜像所需的所有命令

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





- `docker ps`:  List all the running containers, including the ID for each container.  The container id is a unique alphanumeric number for each container, and it is needed in many commands.
  `docker ps`：列出所有正在运行的容器，包括每个容器的ID。  容器id是每个容器的唯一字母数字，许多命令都需要它。
- `docker ps -a`: List all the containers, regardless of whether they are running or not.
  `docker ps -a`：列出所有容器，无论它们是否正在运行。
- `docker exec -it <container id> /bin/bash`: Execute the `/bin/bash` command in a running container. We will get a shell prompt. You don't need to type the entire ID string; typing the first few characters will be sufficient, as long as they are unique.
  `docker exec -it <container id> /bin/bash`：在运行容器中执行`/bin/bash`命令。我们将得到一个shell提示符。您不需要键入整个ID字符串;键入前几个字符就足够了，只要它们是唯一的。
- `docker rm <container id>`: Remove a container.
  `docker rm <container id>`：移除容器。

We will statically assign IP addresses to our container. To do that, we need to attach our container to a network first. We can let docker attach our container to the default network. If you can take this option, you can skip the following network-creation step.
我们将静态地为容器分配IP地址。为此，我们需要首先将容器连接到网络。我们可以让docker将我们的容器连接到默认网络。如果您可以选择此选项，则可以跳过以下网络创建步骤。

In many situations, we would like to attach our containers to a custom network. To achieve that, we need to first create a network using the following docker command, which creates a network called seednetwork, and its network prefix is 172.20.0.0/24. We can further use "docker network" command to manage all the created networks (listing, deleting, etc.).
在许多情况下，我们希望将容器连接到自定义网络。为了实现这一点，我们需要首先使用以下docker命令创建一个网络，该命令创建一个名为seednetwork的网络，其网络前缀为172.20.0.0/24。我们可以进一步使用"docker network"命令来管理所有创建的网络（列表，删除等）。

$ docker network create --subnet=172.20.0.0/24 seednetwork

We are now ready to build and run our container. The first command in the following builds a container called seedhost using the Dockerfile in the current directory. The second command starts the container. The flags -it tell Docker we want an interactive session with a tty attached. The --rm option will remove the container when it stops. The --ip option specifies the static IP address, and the --net option specifies the network this container should be attached to.
现在我们已经准备好构建和运行容器了。下面的第一个命令使用当前目录中的seedhost构建一个名为Dockerfile的容器。第二个命令启动容器。标记-it告诉Docker我们想要一个附加了tty的交互式会话。--rm选项将在容器停止时删除该容器。--ip选项指定静态IP地址，--net选项指定容器应连接到的网络。

$ docker build -t seedhost .
$ docker run --net seednetwork --ip 172.20.0.5 --rm -it seedhost



## Build, Start, and Shutdown the Lab Environment 构建、启动和调试实验室环境



```
docker-compose build
docker-compose up
docker-compose down
```

​    

## Alias Included in the SEED VM 包含在SEED VM中



```
dcbuild        # Alias for: docker-compose build
dcup           # Alias for: docker-compose up
dcdown         # Alias for: docker-compose down
dockps         # Alias for: docker ps --format "{{.ID}}  {{.Names}}"
docksh  <id>   # Alias for: docker exec -it <id> /bin/bash
```

​    

## Useful Docker Commands 有用的Docker命令



```
docker network ls              # List all the networks
docker container restart <id>  # Restart a container
docker container stop    <id>  # Stop a container
docker container start   <id>  # Start a container
```





## Writing the写`docker-compose.yml`file文件



With Compose, we use a YAML file called `docker-compose.yml` to configure our containers. Then, with a single command, we can create and start all the containers from your configuration. The following is an example of the file.
使用Compose，我们使用名为`docker-compose.yml`的YAML文件来配置容器。然后，通过一个命令，我们可以从您的配置中创建和启动所有容器。以下是该文件的示例。

```
version: "3"

services:
    HostA:
        build: ./ubuntu_base
        image: seed-ubuntu-base-image
        container_name: host-10.9.0.5
        tty: true
        cap_add:
                - ALL
        networks:
            net-10.9.0.0:
                ipv4_address: 10.9.0.5

    HostB:
        image: seed-ubuntu-base-image
        container_name: host-10.9.0.6
        tty: true
        cap_add:
                - ALL
        networks:
            net-10.9.0.0:
                ipv4_address: 10.9.0.6

    HostC:
        image: seed-ubuntu-base-image
        container_name: host-10.9.0.7
        tty: true
        cap_add:
                - ALL
        networks:
            net-10.9.0.0:
                ipv4_address: 10.9.0.7

networks:
    net-10.9.0.0:
        name: net-10.9.0.0
        ipam:
            config:
                - subnet: 10.9.0.0/24
```

​    

Let us explain explain how it works.让我们解释一下它是如何工作的。

- The `services` section lists all the containers that we want to build and run
  `services`部分列出了我们要构建和运行的所有容器
- The `networks` section lists all the networks that we need to create. Each network is given a name, and the name is used by the container entries.
  `networks`部分列出了我们需要创建的所有网络。每个网络都有一个名称，该名称由容器条目使用。
- The `build` entry: This entry indicates that the container image's folder name, and will use the `Dockerfile` inside to build a container image. If a service does not have a `build` entry, it means the container does not need to build its own image; it uses the existing image specified in the `image` entry. It should be noted that one image can be used by multiple container instances.
  `build`条目：此条目表示容器镜像的文件夹名称，并将使用内部的`Dockerfile`来构建容器镜像。如果一个服务没有`build`条目，这意味着容器不需要构建自己的镜像;它使用`image`条目中指定的现有镜像。应该注意的是，一个镜像可以由多个容器实例使用。
- The `image` entry: The name of the image is specified in this entry. Without this entry, docker will generate a name for this image.
  `image`条目：在此条目中指定图像的名称。如果没有这个条目，docker将为这个镜像生成一个名称。
- The `container_name` entry: After building the image, Compose will start a container instance from this image, and the name of the container instance is specified in this entry. In our naming convention, we attach the IP address to the hostname.
  `container_name`条目：构建镜像后，Compose将从此镜像启动一个容器实例，容器实例的名称在此条目中指定。在我们的命名约定中，我们将IP地址附加到主机名。
- `tty: true`: Indicate that when running the container, use the `-t` option, which is necessary for getting a shell prompt on the container later on.
  `tty: true`：注意在运行容器时，使用`-t`选项，这是稍后在容器上获得shell提示所必需的。
- The `networks` entry: It specifies the name of the networks that this container is attached to, along with the IP address assigned to the container. Multiple networks can be attached to a container.
  `networks`条目：它指定该容器所连接的网络的名称，沿着分配给容器的IP地址。多个网络可以连接到一个容器。

**Note**: When Docker creates a network, it automatically attaches the host machine (i.e., the VM) to the network, and gives the `.1` as its IP address. Namely, for the `10.9.0.0/24` network, the host machine's IP address is `10.9.0.1`. Therefore, the host machine can directly communicate with all the containers.
注意：当Docker创建网络时，它会自动连接主机（即，虚拟机）发送到网络，并给出`.1`作为其IP地址。也就是说，对于`10.9.0.0/24`网络，主机的IP地址是`10.9.0.1`。因此，主机可以直接与所有容器通信。



# Building, Starting, Stopping Containers 构建、启动和停止容器



## Building the Containers 构建容器



We can use the following commands to build the containers first. This command will build the containers specified in the `docker-compose.yml` file.  To use a different configuration file, use the `-f` option.
我们可以使用以下命令来构建容器。此命令将构建在`docker-compose.yml`文件中指定的容器。  要使用不同的配置文件，请使用`-f`选项。

```
$ docker-compose build
$ docker-compose -f anotherfile.yml build
```

​    

## Start All the Containers 启动所有容器



We can run Compose's `up` command to start all the containers specified in the `docker-compose.yml` file. Make sure to run this command in the same folder as `docker-compose.yml`.
我们可以运行Compose的`up`命令来启动`docker-compose.yml`文件中指定的所有容器。确保在与`docker-compose.yml`相同的文件夹中运行此命令。

```
$ docker-compose up
Creating network "net-10.9.0.0" with the default driver
Creating host-10.9.0.7 ... done
Creating host-10.9.0.6 ... done
Creating host-10.9.0.5 ... done
Attaching to host-10.9.0.6, host-10.9.0.7, host-10.9.0.5
... (blocked here) ...
```

​    

## Stopping All the Containers 停止所有容器



To stop all the containers, we can use `Ctrl-C` to stop the `"docker-compose up"` command, that will stop all the containers, but without removing them. If we want to remove them, we can run Compose's `down` command.
要停止所有容器，我们可以使用`Ctrl-C`停止`"docker-compose up"`命令，这将停止所有容器，但不删除它们。如果我们想删除它们，我们可以运行Compose的`down`命令。

```
Attaching to host-10.9.0.6, host-10.9.0.7, host-10.9.0.5
^CGracefully stopping... (press Ctrl+C again to force)
Stopping host-10.9.0.5 ...
Stopping host-10.9.0.7 ...
Stopping host-10.9.0.6 ...

$ docker-compose down
Removing host-10.9.0.5 ... done
Removing host-10.9.0.7 ... done
Removing host-10.9.0.6 ... done
Removing network net-10.9.0.0
```

​    

Another way to do this is to go to a different terminal (but still in the same folder as `docker-compose.yml`), and run Compose's `down` command. That will stop and removing all the containers.
另一种方法是转到另一个终端（但仍然与`docker-compose.yml`在同一个文件夹中），然后运行Compose的`down`命令。它会停下来并移走所有的容器。

```
$ docker-compose down
Stopping host-10.9.0.7 ... done
Stopping host-10.9.0.6 ... done
Stopping host-10.9.0.5 ... done
Removing host-10.9.0.7 ... done
Removing host-10.9.0.6 ... done
Removing host-10.9.0.5 ... done
Removing network net-10.9.0.0
```





# Running commands on a running container 在正在运行的容器上运行命令



All the containers will run in the background. If we need to run some commands in a container, we just need to first find out this container's ID using the `docker ps` command, and then use the `docker exec` command to run a `bash` shell inside the container. If we use the `-it` option, we will get the interactive shell (a root shell). See the following.
所有容器都将在后台运行。如果我们需要在容器中运行一些命令，我们只需要首先使用`docker ps`命令找到这个容器的ID，然后使用`docker exec`命令在容器中运行一个`bash` shell。如果我们使用`-it`选项，我们将获得交互式shell（根shell）。参阅以下.

```
$ docker ps
CONTAINER ID        NAMES       ...
bcff498d0b1f     host-10.9.0.6  ...
1e122cd314c7     host-10.9.0.5  ...
31bd91496f62     host-10.9.0.7  ...

$ docker exec -it 1e /bin/bash
root@1e122cd314c7:/#
```

​    

It should be noted that in the `docker exec` command, we did not type the full container ID; we only type the first two characters. As long a prefix is unique among all the container IDs, we only need to type the prefix.
应该注意的是，在`docker exec`命令中，我们没有输入完整的容器ID;我们只输入前两个字符。只要前缀在所有容器ID中是唯一的，我们就只需要输入前缀。





# Copy files between container and host 在容器和主机之间复制文件



Very often, we need to transfer files between a container and the hosting machine. This can be easily done using the `docker cp` command. See the following example.
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