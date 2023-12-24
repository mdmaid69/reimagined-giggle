import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a