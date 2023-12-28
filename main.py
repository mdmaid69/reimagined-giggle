import math
def calculate_gamma_function(x):
        return math.gamma(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a