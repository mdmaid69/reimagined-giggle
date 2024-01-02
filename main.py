import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)