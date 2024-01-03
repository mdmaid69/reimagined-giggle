import math
def calculate_arc_sine(x):
        return math.asin(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)