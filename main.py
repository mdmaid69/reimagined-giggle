import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable