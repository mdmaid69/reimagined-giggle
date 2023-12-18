import math
def calculate_sign(x):
        return math.copysign(1, x)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))