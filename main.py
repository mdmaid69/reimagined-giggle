import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)