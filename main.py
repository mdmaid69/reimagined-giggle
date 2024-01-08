def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])