import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def get_bytes_from_array(array):
        return array.tobytes()