import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a