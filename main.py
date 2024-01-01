def is_even(n):
        return n % 2 == 0
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)