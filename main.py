import array
def set_array_item(array, i, item):
        array[i] = item
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)