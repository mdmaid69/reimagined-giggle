import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def pop_from_array(array, i=-1):
        return array.pop(i)