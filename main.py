import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)