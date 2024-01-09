def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a