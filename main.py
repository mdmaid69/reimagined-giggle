import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)