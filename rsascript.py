from pwn import *
from Crypto.Util.number import *
import numpy
import math
conn = remote("rsa.challs.cyberchallenge.it",9040)
conn.recvuntil("Level 1")
conn.recvline()
p=conn.recvline()
q=conn.recvline()
a=conn.recvline()
p=p.replace(b"p =",b"")
q=q.replace(b"q =",b"")
p=int(p)
q=int(q)
n=p*q
n=str(n)+"\n"
n=n.encode()
conn.send(n) #Invio il primo risultato p*q
print(p)
print(q)
print(n)
print(conn.recvline())
print(conn.recvline())
message=conn.recvline()
print(message)
message=message.replace(b"message = ",b"")
message=message.replace(b"\n",b"")
print(conn.recvline())


c=int.from_bytes(message, 'big')
print(int.from_bytes(message, 'big'))
c=str(c)+"\n"
c=c.encode()
conn.send(c)	#Invio secondo risultato cifrato
print(conn.recvline())

#livello 3
print(conn.recvline())
p=conn.recvline()
p=p.replace(b"p = ",b"")
p=p.replace(b"\n",b"")
p=int(p)
print("p = ",p)
q=conn.recvline()
q=q.replace(b"q = ",b"")
q=q.replace(b"\n",b"")
q=int(q)
print("q = ",q)
m=conn.recvline()
m=m.replace(b"m = ",b"")
m=m.replace(b"\n",b"")
m=int(m)
print("m = ",m)
e=conn.recvline()
e=e.replace(b"e = ",b"")
e=e.replace(b"\n",b"")
e=int(e)
print("e = ",e)
print(conn.recvline())
n=p*q
print("n = ",n)
encrypt=pow(m,e)
encrypt=encrypt%n
encrypt=str(encrypt)+"\n"
encrypt=encrypt.encode()
print(encrypt)
conn.send(encrypt)
print(conn.recvline())

#livello 4 parte 1
print(conn.recvline())
p=conn.recvline()
p=p.replace(b"p = ",b"")
p=p.replace(b"\n",b"")
p=int(p)
print("p = ",p)
q=conn.recvline()
q=q.replace(b"q = ",b"")
q=q.replace(b"\n",b"")
q=int(q)
print("q = ",q)
e=conn.recvline()
e=e.replace(b"e = ",b"")
e=e.replace(b"\n",b"")
e=int(e)
print("e = ",e)
print(conn.recvline())
tot=(p-1)*(q-1)
tot=str(tot)+'\n'
tot=tot.encode()
conn.send(tot)
print(conn.recvline())

#livello 4 parte 2
print(conn.recvline())
tot=tot.replace(b"\n",b"")
tot=int(tot)
d=pow(e,-1,tot)	#modular inverse
d=str(d)+'\n'
d=d.encode()
print(d)
conn.send(d)
print(conn.recvline())

#livello 5
print(conn.recvline())
p=conn.recvline()
p=p.replace(b"p = ",b"")
p=p.replace(b"\n",b"")
p=int(p)
print("p = ",p)
q=conn.recvline()
q=q.replace(b"q = ",b"")
q=q.replace(b"\n",b"")
q=int(q)
print("q = ",q)
e=conn.recvline()
e=e.replace(b"e = ",b"")
e=e.replace(b"\n",b"")
e=int(e)
print("e = ",e)
c=conn.recvline()
c=c.replace(b"c = ",b"")
c=c.replace(b"\n",b"")
c=int(c)
print("c = ",c)
print(conn.recvline())

tot=(p-1)*(q-1)
n=p*q
d=pow(e,-1,tot)	#modular inverse
print("n = ",n)
print("tot = ", tot)
print("d = ",d)
m=pow(c,d,n)
m=str(m)+'\n'
m=m.encode()
print(m)
conn.send(m)
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
