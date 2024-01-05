import array
def get_array_typecode(array):
        return array.typecode
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a