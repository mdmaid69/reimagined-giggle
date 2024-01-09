import array
def get_array_as_complex(array):
        return complex(array[0])
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a