import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)