常见cmd命令：

* whoami：查看当前用户名
* ipconfig：查看网卡信息
* shutdown -s -t 0：立刻关机
* net user \[username][password] /add：添加一个新用户
* type [file_name]：查看filename文件内容



防御命令执行漏洞，就是**过滤命令连接符**

- cmd1|cmd2:无论1是否执行成功，2将被执行
- cmd1;cmd2:无论1是否执行成功，2将被执行
- cmd1&cmd2:无论1是否执行成功，2将被执行
- cmd1||cmd2:仅在1执行失败时才执行2
- cmd1&&cmd2:仅在1执行成功后才执行2



渗透测试解决方法：

白盒测试：可以看到源代码，查看源代码过滤机制

黑盒测试：看不到源代码，依次尝试常见命令连接符

Impossible Command Injection Source

```php
<?php

if( isset( $_POST[ 'Submit' ]  ) ) {
    // Check Anti-CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

    // Get input
    $target = $_REQUEST[ 'ip' ];
    $target = stripslashes( $target );//去除用户输入的\

    // Split the IP into 4 octects
    $octet = explode( ".", $target );//把用户输入的数据根据.分开

    // Check IF each octet is an integer判断四个部分是不是数字
    if( ( is_numeric( $octet[0] ) ) && ( is_numeric( $octet[1] ) ) && ( is_numeric( $octet[2] ) ) && ( is_numeric( $octet[3] ) ) && ( sizeof( $octet ) == 4 ) ) {
        // If all 4 octets are int's put the IP back together.验证完后再拼接起来
        $target = $octet[0] . '.' . $octet[1] . '.' . $octet[2] . '.' . $octet[3];

        // Determine OS and execute the ping command.
        if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
            // Windows
            $cmd = shell_exec( 'ping  ' . $target );
        }
        else {
            // *nix
            $cmd = shell_exec( 'ping  -c 4 ' . $target );
        }

        // Feedback for the end user
        echo "<pre>{$cmd}</pre>";
    }
    else {
        // Ops. Let the user name theres a mistake
        echo '<pre>ERROR: You have entered an invalid IP.</pre>';
    }
}

// Generate Anti-CSRF token
generateSessionToken();

?>
```

