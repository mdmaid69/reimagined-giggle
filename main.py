def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)