import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a