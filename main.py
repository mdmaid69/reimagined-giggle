import random
def roll_die():
        return random.randint(1, 6)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)