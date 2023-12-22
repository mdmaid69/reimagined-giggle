import array
def extend_array(array, iterable):
        array.extend(iterable)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)