import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius