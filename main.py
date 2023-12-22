import random
print(random.randint(0, 100))
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)