import math
def calculate_sign(x):
        return math.copysign(1, x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a