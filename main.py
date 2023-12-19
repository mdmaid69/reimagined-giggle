import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"