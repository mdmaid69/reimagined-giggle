import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)