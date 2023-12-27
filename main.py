def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)