import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)