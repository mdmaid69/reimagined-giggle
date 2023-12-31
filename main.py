import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time