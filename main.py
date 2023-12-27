import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)