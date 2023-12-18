import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)