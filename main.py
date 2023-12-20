import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import array
def get_bytes_from_array(array):
        return array.tobytes()