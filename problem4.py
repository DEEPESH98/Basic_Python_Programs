import os

def checkDigit(name):
    for char in name:
        a = char.isdigit()
 return a
        
n=input('Enter any name : ')
if not checkDigit(n):
    pas="hello"+n
    user="useradd -p $(openssl passwd -1 "+pas+") "+n
    os.system(user)

else:
    print("user Cannot be created")
