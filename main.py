import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a