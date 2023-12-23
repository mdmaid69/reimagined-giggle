import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)