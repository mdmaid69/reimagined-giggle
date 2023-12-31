import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)