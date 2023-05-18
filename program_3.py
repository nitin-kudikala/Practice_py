#Author: Nitin
# 9Nov2022
#Program to print the directory content

import os

a =55
b='abc'
d="450"
e='''Nitin's triple quote string's'''
c=55.55

#e[5]='d' -> This does not work

print(os.listdir())
print(os.cpu_count()) #find the number of CPU
print(type(a))
print(a+ int(d))#Type casting example
par = input("Enter your name:")
print('Hello '+par)
print(a[:8] ) # 'Welcome '
print(a[0:8:2]) 
