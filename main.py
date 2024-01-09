import array
def get_array_as_list(array):
        return list(array)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a