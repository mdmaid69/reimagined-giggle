import array
def remove_from_array(array, item):
        array.remove(item)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)