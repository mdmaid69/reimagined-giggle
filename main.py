import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a