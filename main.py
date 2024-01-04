def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)