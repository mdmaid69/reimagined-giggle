import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)