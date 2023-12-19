import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def get_array_as_bytes(array):
        return bytes(array)