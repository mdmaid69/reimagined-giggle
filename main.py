import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))