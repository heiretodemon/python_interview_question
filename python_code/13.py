# V1.0
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)

# V2.0
l3 = list(set(l1))
l3.sort(key=l1.index)
print(l3)

# v3.0
l4 = sorted(set(l1), key=l1.index)
print(l4)

# v4.0
l5 = []
for i in l1:
    if not i in l5:
        l5.append(i)
print(l5)
