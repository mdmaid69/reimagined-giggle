import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a