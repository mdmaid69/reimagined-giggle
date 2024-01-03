import array
def get_array_as_frozenset(array):
        return frozenset(array)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)