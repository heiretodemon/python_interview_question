fact =map(lambda x : 1 if x == 0 or x == 1 else x * fact(x - 1))
