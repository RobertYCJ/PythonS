#!/usr/bin/python3
a = {"a":1,"b":2,"c":3,"d":2,"e":3,"f":2}
#new_a = {v : k for k, v in a.items()}
sum = 0
for i in a:
    sum = sum + a[i]
print(sum)