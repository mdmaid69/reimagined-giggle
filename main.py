import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a