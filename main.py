import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)