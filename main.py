import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)