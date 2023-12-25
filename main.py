import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a