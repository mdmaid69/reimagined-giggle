import array
def get_array_as_float(array):
        return float(array[0])
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a