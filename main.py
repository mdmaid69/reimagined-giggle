import array
def get_array_as_set(array):
        return set(array)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a