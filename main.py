import array
def convert_array_to_list(array):
        return array.tolist()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)