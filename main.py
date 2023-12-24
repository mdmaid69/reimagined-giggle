import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def get_array_typecode(array):
        return array.typecode