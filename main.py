import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)