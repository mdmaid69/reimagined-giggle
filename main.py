import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)