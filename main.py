import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))