import array
def get_array_as_float(array):
        return float(array[0])
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)