import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a