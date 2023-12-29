import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)