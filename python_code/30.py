def del_overlap1(ls):
    # use set()函数
    l = set(ls)
    print(l)

def del_overlap2(ls):
    # 最简单的方法，一个个判断
    l2 = []
    for i in ls:
        if i not in l2:
            l2.append(i)
    print(l2)

def del_overlap3(ls):
    # 字典
    temp = {}
    temp = temp.fromkeys(ls, None) 
    #转化为字典类型，在此方向转换过程中不允许同类型key对应多个value,当发生冲突时，取最后的赋值，且其value均为None
    l3 = list(temp.keys())  # 返回所有的key
    print(l3)
    
if __name__ == "__main__":
    a = [1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
    del_overlap1(a)
    del_overlap2(a)
    del_overlap3(a)