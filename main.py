import math
def calculate_arc_tangent(x):
        return math.atan(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)