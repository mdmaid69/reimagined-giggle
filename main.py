import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)