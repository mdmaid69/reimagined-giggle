import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)