import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def remove_from_array(array, item):
        array.remove(item)