def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"