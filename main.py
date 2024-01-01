import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)