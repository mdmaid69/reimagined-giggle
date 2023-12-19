import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a