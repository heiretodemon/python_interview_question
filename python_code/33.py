list_data = [1,2,5,8,10,3,18,6,20]

newlist = [i for i in list_data[::2] if i%2 == 0]
print(newlist)