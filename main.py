import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)