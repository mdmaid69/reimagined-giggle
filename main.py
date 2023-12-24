import array
def extend_array(array, iterable):
        array.extend(iterable)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}