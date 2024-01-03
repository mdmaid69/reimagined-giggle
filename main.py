import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def get_array_as_complex(array):
        return complex(array[0])