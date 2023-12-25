import array
def iterate_over_array(array):
        for item in array:
        print(item)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)