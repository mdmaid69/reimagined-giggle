import math
def calculate_gamma_function(x):
        return math.gamma(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a