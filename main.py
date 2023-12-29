import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)