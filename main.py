import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))