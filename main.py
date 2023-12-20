import array
def get_bytes_from_array(array):
        return array.tobytes()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a