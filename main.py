import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a