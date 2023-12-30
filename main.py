import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)