import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)