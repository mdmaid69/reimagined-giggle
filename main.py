import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)