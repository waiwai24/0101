
lambda:
```python
#-----------------------------------------------------------------------------------------
it      = lambda                    : p.interactive()
sd      = lambda data               : p.send((data))
sa     	= lambda delim,data         : p.sendafter((delim), (data))
sl      = lambda data               : p.sendline((data))
sla     = lambda delim,data         : p.sendlineafter((delim), (data))
r       = lambda numb=4096          : p.recv(numb)
ru      = lambda delims, drop=False : p.recvuntil(delims, drop)
rl      = lambda                    : p.recvline()
l       = lambda str1               : log.success(str1)
li      = lambda str1,data1         : log.success(str1+' ========> '+hex(data1))
uu32    = lambda data               : u32(data.ljust(4, b"\x00"))
uu64    = lambda data               : u64(data.ljust(8, b"\x00"))
n64     = lambda x                  : (x + 0x10000000000000000) & 0xFFFFFFFFFFFFFFFF
dbg     = lambda                    : gdb.attach(p) / pause()
u32Leakbase = lambda offset         : u32(ru(b"\xf7")[-4:]) - offset
u64Leakbase = lambda offset         : u64(ru(b"\x7f")[-6:].ljust(8, b"\x00")) - offset
#-----------------------------------------------------------------------------------------
```

other:

```
gdb.attach(proc.pidof(p)[0])
pause()
```



exp：

```python
from pwn import *
from LibcSearcher import *
# patchelf --set-interpreter new_ld_address file_path
# patchelf --replace-needed old_libc.so.6 new_libc.so.6 file_path
# pycharm # ctrl+/

elf_path = './pwn'
libc_path = './libc.so.6'
elf = ELF(elf_path, checksec=False)
libc = ELF(libc_path)
context(arch=elf.arch, os=elf.os, log_level="debug")
# context.terminal = ['tmux','splitw','-h']
ip = '8.147.135.93'
port = 37051

local = 1
if local:
    p = process([elf_path])
else:
    p = remote(ip, port)

# session = ssh(host='node5.buuoj.cn', port=26482, user='CTFMan', password='guest')
# p = session.process(['./vuln'])
#-----------------------------------------------------------------------------------------
it      = lambda                    : p.interactive()
sd      = lambda data               : p.send((data))
sa     	= lambda delim,data         : p.sendafter((delim), (data))
sl      = lambda data               : p.sendline((data))
sla     = lambda delim,data         : p.sendlineafter((delim), (data))
r       = lambda numb=4096          : p.recv(numb)
ru      = lambda delims, drop=False : p.recvuntil(delims, drop)
rl      = lambda                    : p.recvline()
l       = lambda str1               : log.success(str1)
li      = lambda str1,data1         : log.success(str1+' ========> '+hex(data1))
uu32    = lambda data               : u32(data.ljust(4, b"\x00"))
uu64    = lambda data               : u64(data.ljust(8, b"\x00"))
n64     = lambda x                  : (x + 0x10000000000000000) & 0xFFFFFFFFFFFFFFFF
dbg     = lambda                    : gdb.attach(p) / pause()
u32Leakbase = lambda offset         : u32(ru(b"\xf7")[-4:]) - offset
u64Leakbase = lambda offset         : u64(ru(b"\x7f")[-6:].ljust(8, b"\x00")) - offset
#-----------------------------------------------------------------------------------------

def add_chunk(index, size):
    sla(b"choice:\n", b"1")
    sla(b"index:\n", str(index).encode())
    sla(b"size:\n", str(size).encode())

def delete_chunk(index):
    sla(b"choice:\n", b"2")
    sla(b"index:\n", str(index).encode())

def edit_chunk(index, content):
    sla(b"choice:\n", b"3")
    sla(b"index:\n", str(index).encode())
    sla(b"length:\n", str(len(content)).encode())
    sa(b"content:\n", content)

def show_chunk(index):
    sla(b"choice:\n", b"4")
    sla(b"index:\n", str(index).encode())

def exit_p():
    sla(b"choice:\n", b"5")

# use LibcSearcher get libc base addr
libc = LibcSearcher("puts", puts_addr)
libc.add_condition("printf", printf_addr)
libc_base = puts_addr - libc.dump("puts")
bin_sh = libc_base + libc.dump("str_bin_sh")
system_addr = libc_base + libc.dump("system")

gdb.attach(p)
pause()
p.interactive()
```

