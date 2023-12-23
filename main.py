import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a