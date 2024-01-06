import array
def get_array_buffer_info(array):
        return array.buffer_info()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)