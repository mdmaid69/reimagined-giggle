import array
def get_array_as_tuple(array):
        return tuple(array)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a