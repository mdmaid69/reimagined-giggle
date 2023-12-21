import array
def get_array_buffer_info(array):
        return array.buffer_info()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}