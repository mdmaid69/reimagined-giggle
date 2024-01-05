import math
def calculate_sign(x):
        return math.copysign(1, x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)