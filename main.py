import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)