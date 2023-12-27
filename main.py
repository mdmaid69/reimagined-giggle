import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a