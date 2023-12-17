import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a