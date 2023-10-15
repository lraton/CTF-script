#!/usr/bin/env python
import pyzipper

with pyzipper.AESZipFile(".zip",'r') as zf:
	with open('rockyou.txt', 'r') as wordlist:
		for password in wordlist:
			password = password.strip()
			try:
				print(password)
				zf.extractall(path='/path', pwd = bytes(password, 'utf-8'))
			except:
				continue
			else:
				wordlist.seek(0)
				break