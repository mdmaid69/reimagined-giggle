import array
def get_array_as_bytearray(array):
        return bytearray(array)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)