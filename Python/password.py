from hashlib import *
# The above will give you a hash of MYSTRING

tryuser = input("What will your user be?")
trypass = input("What will your password be?")

MYSTRING = {"MYSTRING":[trypass]}
# MYSTRING.append(x) 

new = sha256('MYSTRING'.encode('utf-8')).hexdigest()
NEWDICTIONARY = {"NEWSTRING":[new]}


newu2 = input("What is your user?")
newp2 = input("What is your pass?")

if (newp2 == NEWDICTIONARY[0]):
	print ("congrats")
else:
	print("get out")

print(MYSTRING)
print(new)
