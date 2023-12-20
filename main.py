import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def convert_to_hex(n):
        return hex(n)