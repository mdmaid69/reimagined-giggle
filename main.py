import array
def get_array_as_int(array):
        return int(array[0])
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a