import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))