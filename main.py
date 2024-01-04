import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)