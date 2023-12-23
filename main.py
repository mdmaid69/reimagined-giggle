import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import math
def calculate_combinations(n, k):
        return math.comb(n, k)