def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)