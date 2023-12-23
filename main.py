import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a