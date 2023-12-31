def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
n = 10
print("Powers of 2:", [2**x for x in range(n)])