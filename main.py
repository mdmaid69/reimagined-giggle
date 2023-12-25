import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable