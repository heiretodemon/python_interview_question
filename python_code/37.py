def func1(l):
    print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 
        and 20 - int(x) or int(x))))
# %2==0 and 20 -int(x)均是针对偶数的，前者不用说后者表明对每个偶数都进行减数运算后
# 可以保证偶数在进行顺序排序时都大于奇数，能将其排在奇数后面

def func2(l):
    if isinstance(l,str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    print(''.join(str(j) for j in l))

if __name__ == '__main__':
    l = '1982376455'
    func1(l)