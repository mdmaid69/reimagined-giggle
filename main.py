import array
def get_string_from_array(array):
        return array.tobytes()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a