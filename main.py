import array
def get_array_as_repr(array):
        return repr(array)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a