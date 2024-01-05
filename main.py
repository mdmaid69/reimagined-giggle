import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import math
def calculate_sign(x):
        return math.copysign(1, x)