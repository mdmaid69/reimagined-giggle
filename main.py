import array
def check_if_array_contains_item(array, item):
        return item in array
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a