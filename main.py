import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)