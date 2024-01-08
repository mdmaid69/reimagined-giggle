import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))