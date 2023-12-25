import array
def check_if_array_contains_item(array, item):
        return item in array
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a