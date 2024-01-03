import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a