import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a