import math
def calculate_error_function(x):
        return math.erf(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a