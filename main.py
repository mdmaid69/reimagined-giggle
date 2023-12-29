import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def check_if_array_contains_item(array, item):
        return item in array