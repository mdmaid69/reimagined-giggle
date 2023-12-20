def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])