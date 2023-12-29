import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)