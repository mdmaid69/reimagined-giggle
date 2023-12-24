import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)