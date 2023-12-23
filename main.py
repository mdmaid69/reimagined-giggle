import array
def convert_array_to_list(array):
        return array.tolist()
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a