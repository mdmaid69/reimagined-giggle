import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)