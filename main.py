import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def set_array_item(array, i, item):
        array[i] = item