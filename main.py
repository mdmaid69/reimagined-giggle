import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"