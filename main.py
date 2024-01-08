import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))