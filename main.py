import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a