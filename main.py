import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a