import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height