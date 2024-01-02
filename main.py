import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a