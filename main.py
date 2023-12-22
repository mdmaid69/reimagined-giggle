import math
def calculate_sign(x):
        return math.copysign(1, x)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)