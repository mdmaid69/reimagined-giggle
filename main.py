import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def check_if_array_contains_item(array, item):
        return item in array