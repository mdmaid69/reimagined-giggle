import array
def get_array_as_float(array):
        return float(array[0])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)