import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}