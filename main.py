import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)