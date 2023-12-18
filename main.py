print([x**2 for x in range(10)])
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)