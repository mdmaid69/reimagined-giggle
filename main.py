import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array