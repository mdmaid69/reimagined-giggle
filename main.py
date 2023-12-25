import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height