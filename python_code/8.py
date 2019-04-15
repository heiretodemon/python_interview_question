str1 = "k:1|k1:2|k2:3|k3:4"

def str2dict(string):
    dict1 = {}
    for terms in string.split('|'):
        key, value = terms.split(':')
        dict1[key] = value
    return dict1

print(str2dict(str1))