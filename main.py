import math
def calculate_absolute_value(x):
        return math.fabs(x)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a