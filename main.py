import array
def get_array_as_bytes(array):
        return bytes(array)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)