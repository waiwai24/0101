# Unauthorized Access Leads to Sensitive Information Leakage in Vaelsys V4 Platform

BUG_Author: waiwai

Affected Version: v4.1.0 

Vendor：[Vaelsys](https://vaelsys.com/)

Product: Vaelsys V4 

Vulnerability Files: /grid/vgrid_server.php

## Description

In the `vgrid_server.php` interface of the Vaelsys V4 Platform, there exists a serious unauthorized access vulnerability. Attackers can exploit this vulnerability to obtain MD4 password hash values of all system users, and this encryption is insecure.

## POC

xAJAX parameter description: xajaxargs[]=1: The first user (usually the admin user). Through enumeration, it's possible to obtain the MD4-encrypted hash values of all users' passwords.

![image-20250716162508572](./assets/Unauthorized_Access_Leads_to_Sensitive_Information_Leakage_in_Vaelsys_V4_Platform/image-20250716162508572.png)

![屏幕截图 2025-07-16 150451](./assets/Unauthorized_Access_Leads_to_Sensitive_Information_Leakage_in_Vaelsys_V4_Platform/1111111111.png)