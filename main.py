n = 10
print("Square numbers:", [x**2 for x in range(n)])
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)