# beebee

Try my beebee challenge.





# broken_simulator

Have you ever PWNED a real-world project? Write your mips assembly to get /flag. Please have a look at `README` in the attachment first.





# broken_compiler

Before working on the real-world challenge, let's warm up first. Write your C program to read /flag. Please have a look at `README` in the attachment first.





# trust_storage

听说ATF是安全世界，有人在BL31里实现了一个"安全存储"功能，但他真的安全吗



# Alimem

A module full of bugs



# runes

Show me your runes.

hint：

- No intended vulnerability in the bzImage/kernel, please exploit the userspace chal binary.
  hint
- As the challenge's name implies, you need to focus on the `syscall` aka rune in this challenge. Find a way to **weaken the dark dragon's power** once your character becomes strong enough.
  hint
- All syscall numbers（系统调用号） used in the intended solution are under 200 and relatively well used.



从 Linux 内核 4.2 开始，系统调用表从 `arch/x86/syscalls/syscall_64.tbl` 移动到了 `arch/x86/entry/syscalls/syscall_64.tbl`

`sys_call_table`：定义在 `arch/x86/kernel/syscall_64.c` 中，是一个函数指针数组，存储了所有系统调用的实现