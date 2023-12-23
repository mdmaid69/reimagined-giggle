import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable