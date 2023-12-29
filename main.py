import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)