
lambda:
```python
#-----------------------------------------------------------------------------------------
it      = lambda                    :p.interactive()
sd      = lambda data               :p.send((data))
sa     	= lambda delim,data         :p.sendafter((delim), (data)) 
sl      = lambda data               :p.sendline((data)) 
sla     = lambda delim,data         :p.sendlineafter((delim), (data)) 
r       = lambda numb=4096          :p.recv(numb)
ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)
bp      = lambda bkp                :pdbg.bp(bkp)
l       = lambda str1               :log.success(str1)
li      = lambda str1,data1         :log.success(str1+'========>'+hex(data1))
uu32    = lambda data               :u32(data.ljust(4, b'\x00'))
uu64    = lambda data               :u64(data.ljust(8, b'\x00'))	
u32Leakbase = lambda offset         :u32(ru("\xf7")[-4: ]) - offset
u64Leakbase = lambda offset         :u64(ru("\x7f")[-6: ].ljust(8, b'\x00')) - offset
```

other:

```
gdb.attach(proc.pidof(p)[0])
pause()
```

