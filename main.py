import math
def calculate_arc_sine(x):
        return math.asin(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a