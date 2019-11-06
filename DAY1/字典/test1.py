#!/usr/bin/python3
a = {"a":1,"b":2,"c":3,"d":2,"e":3,"f":2}
b = ()
c = ()
sum = 0
#new_a = {v : k for k, v in a.items()}
for k in a:
    print(k)
for v in a.values():
    print(v)

#for k,v in a:


for i in a:
    sum = sum + a[i]
print(sum)