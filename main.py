import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)