def merge_sort(l1, l2):
    tmp = []
    i,j =0,0
    while i<len(l1) and j<len(l2):
        if l1[i] < l2[j]:
            tmp.append(l1[i])
            i+=1
            del l1[i]
        else:
            tmp.append(l2[j])
            j+=1
            del l2[j]
    
    while i<len(l1):
        tmp.append(l1[i])
        i+=1
        del l1[i]

    while j<len(l2):
        tmp.append(l2[j])
        j+=1
        del l2[j]
    return tmp
    