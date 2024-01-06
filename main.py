import array
def get_array_item_count(array, item):
        return array.count(item)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)