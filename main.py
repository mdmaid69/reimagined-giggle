import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_logarithm(base, x):
        return math.log(x, base)