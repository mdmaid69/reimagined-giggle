import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a