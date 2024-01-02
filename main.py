import math
def calculate_absolute_value(x):
        return math.fabs(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)