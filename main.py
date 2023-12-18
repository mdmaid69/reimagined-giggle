import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)