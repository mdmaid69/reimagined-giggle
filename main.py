import array
def get_array_itemsize(array):
        return array.itemsize
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a