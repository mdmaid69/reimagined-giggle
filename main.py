import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a