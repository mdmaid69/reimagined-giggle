import array
def get_array_as_frozenset(array):
        return frozenset(array)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)