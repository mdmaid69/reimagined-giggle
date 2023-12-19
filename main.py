import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)