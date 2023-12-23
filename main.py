import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)