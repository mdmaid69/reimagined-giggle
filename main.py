import array
def get_array_buffer_info(array):
        return array.buffer_info()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a