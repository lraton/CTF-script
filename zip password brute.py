
import pyzipper
import itertools

# Define the characters to bruteforce
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_[{\/?.>,<=+!@#$%^&*()}];:'  # You can customize this to include symbols or other characters

# Define the length of the password
password_length = 3
for x in range(1):
    if x == 0:
        password1 = '900802jfeng@veryrealmail.com'
    
# Generate and print all possible combinations
    for combo in itertools.product(characters, repeat=password_length):
        password = ''.join(combo)

        password2 = 'R3ply!'
        passw=password1+password+password2
        print(passw)
        try:
            with pyzipper.AESZipFile('important_dental_information.zip') as zf:
                zf.extractall(path='', pwd = bytes(passw, 'utf-8'))
                break
        except:
            print('Password ' + passw + ' failed')


