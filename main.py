import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)