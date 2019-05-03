def func1(l):
    print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 
        and 20 - int(x) or int(x))))

def func2(l):
    if isinstance(l,str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    print(''.join(str(j) for j in l))

if __name__ == '__main__':
    l = '1982376455'
    func2(l)