import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)