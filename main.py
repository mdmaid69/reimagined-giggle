def calculate_area(radius):
        return 3.14 * radius * radius
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a