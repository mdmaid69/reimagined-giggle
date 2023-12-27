def calculate_area(radius):
        return 3.14 * radius * radius
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a