# 不带参数的装饰器, 参考链接：https://foofish.net/decorator-with-paramter.html
def new_func(func):
    def wrapper(username):
        name = func(username)
        return "hello " + name
    return wrapper

@new_func
def my_upper(text):
    text = text.upper()
    return text

print(my_upper("wolf"))

# 带定长参数的装饰器
def new_func1(func):
    def wrapper(username, pwd):
        if username == 'wolf' and pwd == '123456':
            print('确认通过')
            return func()
        else:
            print('用户或密码错误')
            return
    return wrapper

@new_func1
def verify():
    print('开始执行')

verify('wolf', '123456')
        
# 带不定长参数的装饰器
def new_func2(func):
    def wrapper(*args):
        if args:
            num = len(args)
            print('此系统包含', end='') # end=''表示末尾不换行，加空格
            for arg in args:
                print(arg, ' ', end='')
            print('wait', num, 'arg')
            return func()
        else:
            print('用户或密码错误')
            return func()
    return wrapper

@new_func2
def verify2():
    print('开始执行')

verify2('wolf', '123456')

