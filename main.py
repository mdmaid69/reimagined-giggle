import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array