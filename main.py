import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a