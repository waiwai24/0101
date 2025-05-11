# pwn-docker

实现在一台虚拟机里面拥有完整的各种版本的libc环境，推荐 https://github.com/RoderickChan/docker_pwn_env



创建容器：

```shell
docker run -it -d -v host_path:container_path -p host_port:container_port --cap-add=SYS_PTRACE --name=container-name IMAGE_ID /bin/sh
```

启动容器：

```shell
docker exec -it CONTAINER_ID /bin/sh
```

tmux鼠标滚动

```
tmux set mouse on
```

在tmux中，ctrl+c 和ctrl+v无法进行复制粘贴。

按住shift可以恢复鼠标右键快捷模式

