# 使用new关键字实现
class A(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self):
        pass

A1 = A()
A2 = A()
print(id(A1) == id(A2))

# 使用装饰器

def singleton(cls):
    __instance = {}

    def inner():
        if cls not in __instance:
            __instance[cls] = cls()
        return __instance[cls]
    return inner

@singleton
class B(object):
    def __init__(self):
        pass

B1 = B()
B2 = B()
print(id(B1) == id(B2))