'''
def multi():
    return [lambda x: i*x for i in range(4)]
print([m(3) for m in multi()])
'''
# 关于闭包的理解：https://zhuanlan.zhihu.com/p/22229197
# 但仍存在疑问
from six.moves import   xrange

flist = []
for i in xrange(3):
    def func(x):
        return i*x;
    flist.append(func)
    print(flist)

for f in flist:
    print(f(2))