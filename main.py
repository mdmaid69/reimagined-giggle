import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_absolute_value(x):
        return math.fabs(x)