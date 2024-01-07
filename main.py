import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a