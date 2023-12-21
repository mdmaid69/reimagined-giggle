import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a