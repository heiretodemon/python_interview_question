import os

def get_pycfile(dir, suffix):
    res = []
    for root, _, files in os.walk(dir):
        for filename in files:
            _, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))

    print(res)

get_pycfile("./", ".pyc")