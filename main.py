import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time