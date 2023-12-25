import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))