#!/usr/bin/python3
a = {"a":1,"b":2,"c":3,"d":2,"e":3,"f":2}

same = []
reslt = []
alist = []
blist = []
sum = 0
# new_a = {v : k for k, v in a.items()}
# print(new_a)


for key in a:
    val = a[key]
    if val in same:
        if val in alist:
            pass
        else:
            alist.append(val)
    else:
        # 没有相
        same.append(val)

b = len(alist)


for i in alist:
    for key in a:
        if a[key] == i:
            blist.append(key)
        else:
            pass
    print (i,blist)
    blist = []
        

for i in a:
    sum = sum + a[i]
print(sum)
