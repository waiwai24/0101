# MD5碰撞



## 1.MD5

MD5,即消息摘要算法(英语:MD5 Message-Digest Algorithm)。是一种被广泛使用的密码散列函数,将数据(如一段文字)运算变为另一固定长度值,是散列算法的基础原理,可以产生出一个128位(16字节)的散列值(hash value),用于确保信息传输完整一致。128位不足以把世界上所有消息的摘要毫不重复的计算出来，当然现在16字节（128位）、32字节（256位）的md5也都有，选择位数多的方式可以在一定程度上减少硬碰撞（collision）的可能性
在php中使用md5的方法：
```php
<?php
$str = "hello world!";
echo "str_md5-->",md5($str),"<br/>"; //为字符串计算摘要值
$files = "02.php";
echo "file_md5-->",md5_file($files);//为文件计算摘要值
?>
```
返回结果：
```
str md5->fc3ff98e8c6a0d3087d515c0473f8677
file md5-->e31b4b584dfdf44a6b8df8caa5652dc5
````
**php中的md5默认返回32字节的结果**



## 2.MD5碰撞的原因

* **php弱类型比较**

* 故意伪造签名



## 3.具体使用

### 3.1 MD5弱比较

* php中所有以`oe`开头的字符串，都使用的是科学计数法并且值为`0`
* 常用绕过：
 ```
QNKCDZO //纯字母
0e830400451993494058024219903391
ABJIHVY 
0e755264355178451322893275696586
240610708 //纯数字
0e462097431906509019562988736854
3293867441 
0e471001201303602543921144570260
s878926199a //混合
0e545993274517709034328855841020
s155964671a
0e342768416822451524974117254469
 ```
### 3.2 MD5强比较

* md5强比较，此时如果传入的两个参数不是字符串，而是数组，md5()函数无法解出其数值，而且不会报错，就会得到`===`强比较的值相等
* payload：

```
param1[]=111&param2[]=222
```
```
var_dump(md5("QNKCDZO")==md5("aabg7XSs")); bool(true)
var_dump(md5("QNKCDZO")===md5("aabg7XSs")); bool(false)
var_dump(md5([0])===md5([false])); bool(true)
```

### 3.3 其他

```
HEX样本A
d131dd02c5e6eec4693d9a0698aff95c
2fcab58712467eab4004583eb8fb7f89
55ad340609f4b30283e488832571415a
085125e8f7cdc99fd91dbdf280373c5b
d8823e3156348f5bae6dacd436c919c6
dd53e2b487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080a80d1e
c69821bcb6a8839396f9652b6ff72a70

d131dd02c5e6eec4693d9a0698aff95c
2fcab50712467eab4004583eb8fb7f89
55ad340609f4b30283e4888325f1415a
085125e8f7cdc99fd91dbd7280373c5b
d8823e3156348f5bae6dacd436c919c6
dd53e23487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080280d1e
c69821bcb6a8839396f965ab6ff72a70

两段数据的MD5均为：
79054025255fb1a26e4bc422aef54eb4
```



## 4.工具

[fastcoll](https://github.com/AndSonder/fastcoll)

