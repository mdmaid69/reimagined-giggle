import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)