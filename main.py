import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)