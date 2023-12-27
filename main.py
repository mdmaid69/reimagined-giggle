import random
def roll_die():
        return random.randint(1, 6)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)