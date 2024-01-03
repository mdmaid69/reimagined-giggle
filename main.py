import array
def get_array_as_list(array):
        return list(array)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)