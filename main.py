import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def get_array_as_frozenset(array):
        return frozenset(array)