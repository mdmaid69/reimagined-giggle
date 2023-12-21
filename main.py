import array
def iterate_over_array(array):
        for item in array:
        print(item)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}