import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_area_triangle(b, h):
        return 0.5 * b * h