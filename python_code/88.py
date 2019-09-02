N = int(input())

print ([[x for x in range(1, N)] 
        [i:i+3] for i in range(0, N, 3)])