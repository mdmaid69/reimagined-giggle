import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a