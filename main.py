import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)