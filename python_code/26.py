from functools import reduce
num = sum([1,2,3,10248])
print(num)

# 2
num2 = reduce (lambda x, y: x+y, [1,2,3,10248])
print(num2)