def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
n = 10
print("Powers of 2:", [2**x for x in range(n)])