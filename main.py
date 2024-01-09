import math
def calculate_arc_sine(x):
        return math.asin(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)