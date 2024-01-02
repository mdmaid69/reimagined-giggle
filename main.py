import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))