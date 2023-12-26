import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)