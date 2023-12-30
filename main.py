import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a