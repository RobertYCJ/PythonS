#!/usr/bin/python3
a = "abbecerrc11"
b = ""
d = {}
res = {}
for i in a:
    d[i] =d.get(i,0)+1
for j in d.keys():
    if d[j]>1:
        res[j] = d[j]
for c in res.keys():
    b += str(c)
print(b)


