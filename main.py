import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time