import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def get_array_typecode(array):
        return array.typecode