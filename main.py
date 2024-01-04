import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a