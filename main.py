import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)