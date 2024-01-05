def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a