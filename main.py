def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"