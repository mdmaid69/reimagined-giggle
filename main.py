import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)