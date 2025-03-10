# system 函数探究

定义在 glibc 中的/sysdeps/posic/system.c：

```c
int
__libc_system (const char *line)
{
  if (line == NULL)
    /* Check that we have a command processor available.  It might
       not be available after a chroot(), for example.  */
    return do_system ("exit 0") == 0;

  return do_system (line);
}
weak_alias (__libc_system, system)
```

- 函数名 `__libc_system` 是内部实现名，通过 `weak_alias` 宏映射到公共 API `system()`
- 而 `__libc_system` 是 `do_system` 的前端函数，进行了参数的检查

```c
/* Execute LINE as a shell command, returning its status.  */
static int
do_system (const char *line)
{
  int status, save;
  pid_t pid;
  struct sigaction sa;
#ifndef _LIBC_REENTRANT
  struct sigaction intr, quit;
#endif
  sigset_t omask;

  sa.sa_handler = SIG_IGN;
  sa.sa_flags = 0;
  __sigemptyset (&sa.sa_mask);

  DO_LOCK ();
  if (ADD_REF () == 0)
    {
      if (__sigaction (SIGINT, &sa, &intr) < 0)
	{
	  (void) SUB_REF ();
	  goto out;
	}
      if (__sigaction (SIGQUIT, &sa, &quit) < 0)
	{
	  save = errno;
	  (void) SUB_REF ();
	  goto out_restore_sigint;
	}
    }
  DO_UNLOCK ();

  /* We reuse the bitmap in the 'sa' structure.  */
  __sigaddset (&sa.sa_mask, SIGCHLD);
  save = errno;
  if (__sigprocmask (SIG_BLOCK, &sa.sa_mask, &omask) < 0)
    {
#ifndef _LIBC
      if (errno == ENOSYS)
	__set_errno (save);
      else
#endif
	{
	  DO_LOCK ();
	  if (SUB_REF () == 0)
	    {
	      save = errno;
	      (void) __sigaction (SIGQUIT, &quit, (struct sigaction *) NULL);
	    out_restore_sigint:
	      (void) __sigaction (SIGINT, &intr, (struct sigaction *) NULL);
	      __set_errno (save);
	    }
	out:
	  DO_UNLOCK ();
	  return -1;
	}
    }

#ifdef CLEANUP_HANDLER
  CLEANUP_HANDLER;
#endif

#ifdef FORK
  pid = FORK ();
#else
  pid = __fork ();
#endif
  if (pid == (pid_t) 0)
    {
      /* Child side.  */
      const char *new_argv[4];
      new_argv[0] = SHELL_NAME;
      new_argv[1] = "-c";
      new_argv[2] = line;
      new_argv[3] = NULL;

      /* Restore the signals.  */
      (void) __sigaction (SIGINT, &intr, (struct sigaction *) NULL);
      (void) __sigaction (SIGQUIT, &quit, (struct sigaction *) NULL);
      (void) __sigprocmask (SIG_SETMASK, &omask, (sigset_t *) NULL);
      INIT_LOCK ();

      /* Exec the shell.  */
      (void) __execve (SHELL_PATH, (char *const *) new_argv, __environ);
      _exit (127);
    }
  else if (pid < (pid_t) 0)
    /* The fork failed.  */
    status = -1;
  else
    /* Parent side.  */
    {
      /* Note the system() is a cancellation point.  But since we call
	 waitpid() which itself is a cancellation point we do not
	 have to do anything here.  */
      if (TEMP_FAILURE_RETRY (__waitpid (pid, &status, 0)) != pid)
	status = -1;
    }

#ifdef CLEANUP_HANDLER
  CLEANUP_RESET;
#endif

  save = errno;
  DO_LOCK ();
  if ((SUB_REF () == 0
       && (__sigaction (SIGINT, &intr, (struct sigaction *) NULL)
	   | __sigaction (SIGQUIT, &quit, (struct sigaction *) NULL)) != 0)
      || __sigprocmask (SIG_SETMASK, &omask, (sigset_t *) NULL) != 0)
    {
#ifndef _LIBC
      /* glibc cannot be used on systems without waitpid.  */
      if (errno == ENOSYS)
	__set_errno (save);
      else
#endif
	status = -1;
    }
  DO_UNLOCK ();

  return status;
}
```

```c
#define	SHELL_PATH	"/bin/sh"	/* Path of the shell.  */
#define	SHELL_NAME	"sh"		/* Name to give it.  */
```

* 调用系统调用 fork 产生一个子进程，其中 fork 有两个返回值，父子进程分别执行不同的代码
* 子进程调用 execve 执行 SHELL_PATH 指定的程序，参数通过 new_argv 传递，环境变量为全局变量__environ
* execve执行失败则返回127
* CTF中，通过栈溢出调用system函数有时会失败，有时候的原因是环境变量被覆
