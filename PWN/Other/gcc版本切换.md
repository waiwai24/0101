# gcc版本切换

```shell
$ sudo apt -y install build-essential
```

安装不同的gcc版本

```shell
$ sudo apt -y install gcc-8 g++-8 gcc-9 g++-9
```

更新

```shell
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8 --slave /usr/bin/g++ g++ /usr/bin/g++-8
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9 --slave /usr/bin/g++ g++ /usr/bin/g++-9
```

选择gcc版本

```shell
$ sudo update-alternatives --config gcc
```

