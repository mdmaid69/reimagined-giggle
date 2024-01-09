import collections
def create_ordered_dict():
        return collections.OrderedDict()
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a