import math
def calculate_tangent(x):
        return math.tan(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)