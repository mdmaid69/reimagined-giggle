import array
def get_array_as_repr(array):
        return repr(array)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)