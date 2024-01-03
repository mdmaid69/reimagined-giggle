import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def get_string_from_array(array):
        return array.tobytes()