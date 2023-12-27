import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)