'''
函数嵌套函数
def print_name(name):
    return 'fuck, ' + name

def add_symbol(func1):
    def prt_func(name):
        return '&&&{0}&&&'.format(func1(name))
    return prt_func

if __name__ == "__main__":
    hell = add_symbol(print_name)
    print(hell('world'))

'''

def add_symbol(func1):
    def prt_func(name):
        return '&&&{0}&&&'.format(func1(name))
    return prt_func

@add_symbol
def print_name(name):
    return 'fuck, ' + name

# 这样与上面的函数嵌套函数效果一致，就是将函数和字符串都
# 都作为参数传递给装饰器了

if __name__ == "__main__":
    print (print_name('world'))