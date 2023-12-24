import array
def append_to_array(array, item):
        array.append(item)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)