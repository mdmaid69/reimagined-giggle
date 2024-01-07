import array
def get_list_from_array(array):
        return array.tolist()
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a