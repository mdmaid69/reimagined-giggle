import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable