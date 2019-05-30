import datetime

class TimeException(Exception):
    def __init__(self, exception_info):
        super().__init__()
        self.info = exception_info

    def __str__(self):
        return self.info

def timecheck(func):
    def wrapper(*args, **kwargs):
        if datetime.datetime.now().year == 2019:
            func(*args, **kwargs)
        else:
            raise TimeException("out of time")

    return wrapper

@timecheck
# @在此处的用法相当于timecheck(test()),且当运行到代码时，
# test函数已经消失了，再想调用其属性时会报错
def test(name):
    print('hello {}'.format(name))

if __name__ == "__main__":
    test('world')