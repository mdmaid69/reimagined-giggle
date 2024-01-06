import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def extend_array(array, iterable):
        array.extend(iterable)