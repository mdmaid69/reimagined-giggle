import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import math
def calculate_error_function(x):
        return math.erf(x)