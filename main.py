import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a