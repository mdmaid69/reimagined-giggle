import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)