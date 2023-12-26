import random
print(random.randint(0, 100))
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)