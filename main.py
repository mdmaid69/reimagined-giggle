import random
def roll_die():
        return random.randint(1, 6)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)