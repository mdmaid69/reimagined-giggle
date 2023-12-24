import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)