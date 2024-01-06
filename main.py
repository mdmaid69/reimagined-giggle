import math
def calculate_floor(x):
        return math.floor(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)