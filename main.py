import random
print(random.randint(0, 100))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)