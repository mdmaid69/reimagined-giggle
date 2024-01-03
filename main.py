import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import array
def get_array_as_complex(array):
        return complex(array[0])