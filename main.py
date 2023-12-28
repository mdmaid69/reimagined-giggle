import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def insert_into_array(array, i, item):
        array.insert(i, item)