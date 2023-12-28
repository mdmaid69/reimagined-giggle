import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)