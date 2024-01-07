import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))