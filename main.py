import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a