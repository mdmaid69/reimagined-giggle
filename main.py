import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a