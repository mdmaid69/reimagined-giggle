import random
def generate_random_choice(choices):
        return random.choice(choices)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)