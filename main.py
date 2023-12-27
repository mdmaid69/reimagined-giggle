import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)