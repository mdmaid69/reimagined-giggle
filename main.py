import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)