import array
def get_array_as_tuple(array):
        return tuple(array)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)