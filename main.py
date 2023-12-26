import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}