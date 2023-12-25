import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)