import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a