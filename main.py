import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}