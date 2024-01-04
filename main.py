import array
def convert_array_to_bytes(array):
        return array.tobytes()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)