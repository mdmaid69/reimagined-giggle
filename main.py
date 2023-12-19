import array
def get_array_buffer_info(array):
        return array.buffer_info()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)