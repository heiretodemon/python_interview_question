import os
'''
def get_pycfile(dir, suffix):
    res = []
    for root, _, files in os.walk(dir):
        for filename in files:
            _, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))

    print(res)

get_pycfile("./", ".pyc")
'''

#方法二
def pick(obj):
    if obj.endswith('.pyc'):
        print(obj)

def scan_path(ph):
    file_ls = os.listdir(ph)
    print(file_ls)
    for obj in file_ls:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)
            print(obj)

if __name__ == '__main__':
    path = input("please input dir:")
    scan_path(path)