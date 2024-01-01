import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def extend_array(array, iterable):
        array.extend(iterable)