import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a