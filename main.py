import array
def convert_array_to_list(array):
        return array.tolist()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a