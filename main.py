import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}