# 利用str函数
def atoi(s):
    num = 0
    for i in s:
        for j in range(10):
            if i == str(j):
                num = num*10 + j
    return num

# 利用ord函数
def atoi1(s):
    num = 0
    for i in s:
        num = num*10 + ord(i) - ord('0')
    return num

# 利用eval函数
def atoi2(s):
    num = 0
    for i in s:
        t = "%s * 1 " %i
        n = eval(t)
        num = num * 10 + n
    return num

# 利用reduce函数
from functools import reduce
def atoi3(s):
    return reduce(lambda num, i: num * 10 + ord(i) - ord('0'), s , 0)


if __name__ == '__main__':
    s = "432"
    #print(type(s))
    #s = input ("please input: ")
    print(atoi2(s))
