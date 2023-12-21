import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"