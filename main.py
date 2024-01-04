import array
def extend_array(array, iterable):
        array.extend(iterable)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)