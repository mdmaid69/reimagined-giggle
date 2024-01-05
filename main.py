import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_sign(x):
        return math.copysign(1, x)