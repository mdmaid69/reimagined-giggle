import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)