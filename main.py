import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}