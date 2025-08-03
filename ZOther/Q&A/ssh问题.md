* 配置服务器

  ```shell
  sudo apt install openssh-server
  sudo service ssh restart
  ```

  

* 编译配置文件

  ```shell
  sudo gedit /etc/ssh/sshd_config
  将PermitRootLogin prohibit-password改为PermitRootLogin yes
  ```

* ```shell
  /etc/init.d/ssh restart
  ```

  