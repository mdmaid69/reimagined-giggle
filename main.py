import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))