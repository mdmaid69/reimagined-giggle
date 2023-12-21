import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a