a = [1,2,3,4,5,6,7,8]
print(id(a))
print(id(a[:]))

for i in a[:]:
    if i>5:
        pass
    else :
        a.remove(i)
    print(a)

print('-----------')
print(id(a))

# 方法二：filter
b = filter(lambda x: x>5, a)
print(list(b))

# 方法三： 列表解析
c = [i for i in a if i>5]
print(c)

# 法四：倒序删除
print('----------')
print(id(a))
for i in range(len(a)-1, -1, -1):
    if a[i]>5:
        pass
    else:
        a.remove(a[i])

print(a)
print(id(a))