import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)