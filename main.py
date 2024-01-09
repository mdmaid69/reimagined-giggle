import array
def get_array_typecode(array):
        return array.typecode
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a