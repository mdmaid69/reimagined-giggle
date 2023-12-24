import array
def get_array_as_memoryview(array):
        return memoryview(array)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)