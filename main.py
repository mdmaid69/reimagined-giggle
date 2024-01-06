import array
def get_string_from_array(array):
        return array.tobytes()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)