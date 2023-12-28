import math
def calculate_gamma_function(x):
        return math.gamma(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a