#!/usr/bin/python3
a = "aef1122"
b = input()  #输入字符串
c = len(b)   #输入字符串长度
d = 0        
e = ""       #输出字符串
while d<c or d<len(a):
    if a[d] == b[0].lower():
        e = e + b
        break
    else:
        e = e + a[d]
        d += 1
print(e)
