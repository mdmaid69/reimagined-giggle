import array
def get_array_itemsize(array):
        return array.itemsize
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a