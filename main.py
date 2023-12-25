import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a