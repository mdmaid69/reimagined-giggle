def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)