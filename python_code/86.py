def fib(n):
    prev, cur = 0, 1
    while n>0:
        n -= 1
        yield cur
        prev, cur = cur, cur + prev

if __name__ == "__main__":
    print ([i for i in fib(20)])