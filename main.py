import math
def calculate_sign(x):
        return math.copysign(1, x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a