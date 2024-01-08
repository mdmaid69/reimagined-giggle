import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))