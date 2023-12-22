import array
def convert_array_to_bytes(array):
        return array.tobytes()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a