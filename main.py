import array
def convert_array_to_string(array):
        return array.tostring()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a