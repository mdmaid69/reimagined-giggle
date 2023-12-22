import array
def remove_from_array(array, item):
        array.remove(item)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a