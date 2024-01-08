import math
def calculate_ceiling(x):
        return math.ceil(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)