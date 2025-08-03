1. fast github

2. git clone 出现fatal:无法访问问题解决

   例如 git clone https://github.com/aboul3la/Sublist3r.git 直接进行clone 出现fatal：无法访问的问题

   直接在 中间加上 gitclone.com/

   例如 git clone https://gitclone.com/github.com/aboul3la/Sublist3r.git

   问题得到解决

3. 无法ping通github，返回`Temporary failure in name resolution`

   解决方案：

   ```shell
   echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
   ```

4. 修改host /etc/hosts 
