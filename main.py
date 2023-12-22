import math
def calculate_logarithm_base_e(x):
        return math.log(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)