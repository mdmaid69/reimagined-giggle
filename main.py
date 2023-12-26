import array
def get_array_as_set(array):
        return set(array)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)