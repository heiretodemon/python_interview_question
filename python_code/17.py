# 使用基类new
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, 
    cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)

# 使用装饰器
from functools import wraps

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class FOO(object):
    pass

foo3 = FOO()
foo4 = FOO()
print(foo3 is foo4)