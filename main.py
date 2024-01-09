def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])