import random
def generate_random_choice(choices):
        return random.choice(choices)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)