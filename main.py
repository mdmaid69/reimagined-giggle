import collections
def create_ordered_dict():
        return collections.OrderedDict()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a