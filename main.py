import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))