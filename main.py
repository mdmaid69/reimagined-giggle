import array
def remove_from_array(array, item):
        array.remove(item)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)