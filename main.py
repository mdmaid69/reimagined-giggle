import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def convert_array_to_list(array):
        return array.tolist()