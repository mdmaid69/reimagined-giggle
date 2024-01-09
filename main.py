import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)