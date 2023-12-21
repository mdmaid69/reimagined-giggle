import array
def clear_array(array):
        array *= 0
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)