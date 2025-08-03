打开虚拟机目录，删除以 .lck 结尾的文件

如果还不能打开，打开VMware的安装目录，使用vmware-vdiskmanager.exe工具修复所有的vmdk文件和vmx文件

```
ls "M:\VM\DDC\*.vmdk" | % { .\vmware-vdiskmanager.exe -R $_.FullName }
```

