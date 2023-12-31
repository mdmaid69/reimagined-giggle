import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))