import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a