import array
def get_string_from_array(array):
        return array.tobytes()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)