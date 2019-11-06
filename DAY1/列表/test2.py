#!/usr/bin/python3
a = [13,2,5,1,3]
b = input()
e = []
f = 0


try:
    float(b)
except ValueError:
    print("输入值不为数字")
else:
    for num in a:
         if float(num) > float(b) :
            e.insert(f,num)
            f += 1
    print(e)

    
