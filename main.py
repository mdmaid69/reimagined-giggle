import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def get_list_from_array(array):
        return array.tolist()