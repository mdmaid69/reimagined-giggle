import array
def remove_from_array(array, item):
        array.remove(item)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}