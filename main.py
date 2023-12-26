import array
def append_to_array(array, item):
        array.append(item)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a