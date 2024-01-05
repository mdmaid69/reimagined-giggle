import array
def get_array_item(array, i):
        return array[i]
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a