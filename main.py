import array
def get_array_as_bytes(array):
        return bytes(array)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}