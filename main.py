import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def check_if_array_contains_item(array, item):
        return item in array