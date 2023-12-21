import array
def get_array_slice(array, i, j):
        return array[i:j]
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}