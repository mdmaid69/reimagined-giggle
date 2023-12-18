def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b