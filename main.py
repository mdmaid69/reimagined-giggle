import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)