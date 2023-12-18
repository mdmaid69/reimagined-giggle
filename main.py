import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a