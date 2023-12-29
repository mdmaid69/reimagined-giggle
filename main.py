import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def is_even(n):
        return n % 2 == 0