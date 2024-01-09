import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable