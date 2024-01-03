import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a