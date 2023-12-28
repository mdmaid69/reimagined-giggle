import math
def calculate_exponential(x):
        return math.exp(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)