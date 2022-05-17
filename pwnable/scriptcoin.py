from pwn import *
import time

arr = []

conn = remote("pwnable.kr",9007)
conn.recvuntil("- Ready?")
sleep(3)
print (conn.recvline())
print (conn.recvline())
N,C=conn.recvline().split()
N=N.replace(b"N=",b"")
C=C.replace(b"C=",b"")

def search(N, C):

	ans= -1
	for i in range(0,n,2):
		if(arr[i]!=arr[i+1]):
			ans= arr[i]
			break
	if(arr[n-2]!=arr[n-1]):
		ans = arr[n-1]
	
	conn.sendline("the required element is", ans)
	

print(N)
print(C)



	
