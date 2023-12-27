def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)