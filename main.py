import array
def get_array_item_count(array, item):
        return array.count(item)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)