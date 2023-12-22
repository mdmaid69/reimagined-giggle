import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def get_array_as_set(array):
        return set(array)