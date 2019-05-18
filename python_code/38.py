from functools import reduce

def find_2nd_num_1(num_list):
    '''
    方法1：直接进行逆序排序，找出第二个数即可
    '''
    tmp_list = sorted(num_list, reverse=True)
    return tmp_list[1]

def find_2nd_num_2(num_list):
    '''
    方法2:传统面向过程的思路，设置两个标志位，一个存储最大值，一个存储次大值
    '''
    a = num_list[0]
    b = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > a:
            b = a
            a = num_list[i]
        elif num_list[i] > b:
            b = num_list[i]
    return b

def find_2nd_num_3(num_list):
    num = reduce(lambda ot, x: ot[1]<x and (ot[1], x) or ot[0]< x 
    and (x, ot[1]) or ot, num_list, (0,0))[0]
    return num


if __name__ == '__main__':
    num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
    print(find_2nd_num_3(num_list))
