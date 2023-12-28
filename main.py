import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)