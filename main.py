import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable