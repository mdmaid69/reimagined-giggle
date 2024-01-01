import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)