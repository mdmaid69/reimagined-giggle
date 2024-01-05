def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)