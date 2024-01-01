import array
def remove_from_array(array, item):
        array.remove(item)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a