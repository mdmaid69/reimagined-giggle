import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a