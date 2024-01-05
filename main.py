import array
def get_array_item_count(array, item):
        return array.count(item)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a