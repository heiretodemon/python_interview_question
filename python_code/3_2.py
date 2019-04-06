# 字典推导式
A = {'a':1, 'b':2, 'c':3}
d = {key:value for (key, value) in A.items()}
print(d)

# 列表推导式
ls = [i**2 for i in range(10) if i % 3 == 0]
print(ls)

# 集合推导式(输出结果集合中不会出现重复的)
sq = {i*3 for i in [1,2,2,3,4,5]}
print(sq)