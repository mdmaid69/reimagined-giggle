import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}