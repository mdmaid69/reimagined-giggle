import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)