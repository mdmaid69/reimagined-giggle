import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)