import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)