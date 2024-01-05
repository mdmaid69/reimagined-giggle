import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)