import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a