import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)