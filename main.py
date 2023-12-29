import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a