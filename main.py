import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)