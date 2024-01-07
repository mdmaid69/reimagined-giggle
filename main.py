import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))