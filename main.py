import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height