n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)