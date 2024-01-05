import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3