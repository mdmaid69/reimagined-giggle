import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a