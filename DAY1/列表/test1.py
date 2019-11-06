#!/usr/bin/python3
a = 0
b = ""
while a < 100:
    a += 1
    if a%2 == 1:
        b = b + str(a)
        b = b + ","
    
print(b)