def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
n = 10
print("Powers of 2:", [2**x for x in range(n)])