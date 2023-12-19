import array
def get_bytes_from_array(array):
        return array.tobytes()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}