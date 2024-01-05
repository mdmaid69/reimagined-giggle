import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a