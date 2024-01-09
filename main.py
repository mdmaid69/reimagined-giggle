import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a