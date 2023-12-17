import array
def convert_array_to_unicode(array):
        return array.tounicode()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)