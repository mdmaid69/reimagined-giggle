import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)