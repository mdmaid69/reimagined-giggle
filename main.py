import array
def convert_array_to_list(array):
        return array.tolist()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a