import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a