def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
n = 10
print("Square numbers:", [x**2 for x in range(n)])