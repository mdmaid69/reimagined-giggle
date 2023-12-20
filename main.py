import array
def get_array_as_bytearray(array):
        return bytearray(array)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)