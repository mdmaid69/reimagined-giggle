import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)