from pwn import *

group =[b'\xE8\x05\xd9\x1d', b'\01\01\01\01', b'\01\01\01\01', b'\01\01\01\01', b'\01\01\01\01']

payload =b''.join(group)

print(payload)
s=ssh(host='pwnable.kr', user='col', password='guest', port=2222)
io = s.process(['./col',payload])

info(io.recvline().decode())
