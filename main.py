import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a