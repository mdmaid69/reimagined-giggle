import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a