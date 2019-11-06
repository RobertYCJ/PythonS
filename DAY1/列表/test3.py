#!/usr/bin/python3
a = [1,3,4,2,4]
b = 0
for num in a:
    if num > b:
        b = num
    #     c = str(a.index(num))
    # elif num == b:
    #     c = c + ","
    #     c = c + str(a.index(num))
c = [i for i,x in enumerate(a) if x==b]    
print("索引为：",c)