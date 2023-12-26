import array
def get_array_itemsize(array):
        return array.itemsize
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)