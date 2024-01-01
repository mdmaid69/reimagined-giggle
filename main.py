import array
def get_array_slice(array, i, j):
        return array[i:j]
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a