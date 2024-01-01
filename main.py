import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def iterate_over_array(array):
        for item in array:
        print(item)