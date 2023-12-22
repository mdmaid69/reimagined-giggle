import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)