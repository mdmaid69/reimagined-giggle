import math
def calculate_tangent(x):
        return math.tan(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)