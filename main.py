import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a