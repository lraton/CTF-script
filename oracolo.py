from pwn import*
conn = remote("padding.challs.cyberchallenge.it",9033)
print(conn.recvline())
print(conn.recv())
conn.send(b"1xxxx")
print(conn.recvline())
