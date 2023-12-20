import array
def append_to_array(array, item):
        array.append(item)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a