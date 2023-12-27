import array
def get_list_from_array(array):
        return array.tolist()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a