print([x**2 for x in range(10)])
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)