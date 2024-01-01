import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a