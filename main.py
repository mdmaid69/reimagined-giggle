import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a