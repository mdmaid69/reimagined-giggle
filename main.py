import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a