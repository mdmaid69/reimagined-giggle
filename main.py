import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}