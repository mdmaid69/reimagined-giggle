import array
def extend_array(array, iterable):
        array.extend(iterable)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a