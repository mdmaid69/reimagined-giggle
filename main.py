import array
def get_list_from_array(array):
        return array.tolist()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a