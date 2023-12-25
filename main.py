import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))