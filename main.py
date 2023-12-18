import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def extend_array(array, iterable):
        array.extend(iterable)