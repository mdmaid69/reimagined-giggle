import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a