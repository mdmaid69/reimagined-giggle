import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)