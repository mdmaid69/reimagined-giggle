import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def get_array_as_frozenset(array):
        return frozenset(array)