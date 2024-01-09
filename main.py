n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)