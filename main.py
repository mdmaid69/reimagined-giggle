import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time