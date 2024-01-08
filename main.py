import array
def append_to_array(array, item):
        array.append(item)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}