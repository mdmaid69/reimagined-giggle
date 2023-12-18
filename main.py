import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)