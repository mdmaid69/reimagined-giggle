import array
def convert_array_to_list(array):
        return array.tolist()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a