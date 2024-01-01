import math
def calculate_sign(x):
        return math.copysign(1, x)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"