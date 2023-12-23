import array
def get_array_as_complex(array):
        return complex(array[0])
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a