import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)