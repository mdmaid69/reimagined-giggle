import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)