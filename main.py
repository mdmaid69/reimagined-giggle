def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b