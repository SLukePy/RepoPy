import os
import sys
i=10
print("Hello")

if (i==10):
    print("I= : ",i)

for x in range(1,100):
    if (x%2==0):
        print(x)

mystring="i can be great again, I will do it again"

print(len(mystring))
print(mystring[0:len(mystring)])

print(mystring.capitalize())
print(mystring.upper())

def myfunc1(myf, myl):
    sumnum=myf+myl
    return sumnum

print(myfunc1(40,5))

print("%c",("abc"))


myfile=open("c:\\Temp\\text.txt","wb")
myfile.write(bytes("Write my data into file","UTF-8"))
myfile.close()
myfile1=open("c:\\temp\\text.txt", "r+")
print(myfile1.read())