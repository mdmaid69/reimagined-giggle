def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)