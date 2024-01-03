import array
def get_array_slice(array, i, j):
        return array[i:j]
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a