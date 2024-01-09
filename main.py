import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a