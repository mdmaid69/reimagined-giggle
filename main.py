import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)