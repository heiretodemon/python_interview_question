alist = [{'name':'a', 'age':20}, {'name':'b', 'age':30},
 {'name':'c', 'age':25}]

def age_sort(ls):
    return sorted(ls, key=lambda x:x['age'])

print(age_sort(alist))