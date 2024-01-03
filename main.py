import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"