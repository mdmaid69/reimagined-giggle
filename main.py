print([x**2 for x in range(10)])
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)