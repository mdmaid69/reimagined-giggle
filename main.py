import array
def get_array_as_bytes(array):
        return bytes(array)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)