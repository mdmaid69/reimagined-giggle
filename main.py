import array
def get_array_itemsize(array):
        return array.itemsize
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a