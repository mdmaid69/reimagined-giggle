import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_logarithm(base, x):
        return math.log(x, base)