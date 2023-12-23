import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import math
def calculate_permutations(n, k):
        return math.perm(n, k)