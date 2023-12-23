import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)