import array
def get_array_as_frozenset(array):
        return frozenset(array)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a