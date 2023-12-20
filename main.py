import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import array
def convert_array_to_unicode(array):
        return array.tounicode()