import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)