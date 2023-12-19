import array
def get_array_index(array, item):
        return array.index(item)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)