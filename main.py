import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))