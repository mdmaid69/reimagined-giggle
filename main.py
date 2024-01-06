import math
def calculate_sign(x):
        return math.copysign(1, x)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))