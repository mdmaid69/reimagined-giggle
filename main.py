import array
def get_array_as_frozenset(array):
        return frozenset(array)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)