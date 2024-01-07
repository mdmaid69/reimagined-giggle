import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)