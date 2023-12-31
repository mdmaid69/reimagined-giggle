import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)