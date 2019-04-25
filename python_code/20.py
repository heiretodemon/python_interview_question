def add(num):
    add_sum = sum(range(0,num+1))
    print(add_sum)

if __name__ == '__main__':
    num = input('please input the number:')
    add(int(num))
    