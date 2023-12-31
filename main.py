import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"