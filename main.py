import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)