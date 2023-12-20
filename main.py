import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)