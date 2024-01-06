import math
def calculate_arc_tangent(x):
        return math.atan(x)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)