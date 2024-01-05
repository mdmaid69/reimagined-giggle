import math
def calculate_arc_cosine(x):
        return math.acos(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)