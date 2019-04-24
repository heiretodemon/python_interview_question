import os

def get_pycfile(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))

    print(res)

get_pycfile("./", ".pyc")