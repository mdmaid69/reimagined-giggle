import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)