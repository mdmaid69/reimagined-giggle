import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))