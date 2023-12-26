def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a