def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)