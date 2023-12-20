import math
def calculate_arc_tangent(x):
        return math.atan(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)