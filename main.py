import array
def get_array_index(array, item):
        return array.index(item)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a