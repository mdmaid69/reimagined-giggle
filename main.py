import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a