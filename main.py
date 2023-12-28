import array
def get_list_from_array(array):
        return array.tolist()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}