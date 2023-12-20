import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)