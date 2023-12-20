import array
def get_bytes_from_array(array):
        return array.tobytes()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)