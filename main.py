import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a