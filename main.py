import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)