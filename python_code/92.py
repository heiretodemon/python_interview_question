'''
方法一：
  私有化（通过“属性前置双下划线”实现）
  部分公开：通过公开的方法
'''
class Person:
    def __init__(self):
        self.__age = 18
    
    def getAge(self):
        return self.__age

p = Person()
print(p.getAge())
p.__age = 20
print(p.__dict__)


# 优化方案：装饰器@property.作用：将一些属性的操作方法
# 关联到某一个属性当中
class Person(object):
    def __init__(self):
        self.__age=18

    @property
    def age(self):
        return self.__age

p1 = Person()
print(p1.age)
p1.__age=1
print(p1.age)
print(p1.__dict__)