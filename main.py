import math
def calculate_cosine(x):
        return math.cos(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)