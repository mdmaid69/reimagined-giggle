import math
def calculate_sine(x):
        return math.sin(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)