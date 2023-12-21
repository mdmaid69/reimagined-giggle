import array
def get_array_slice(array, i, j):
        return array[i:j]
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)