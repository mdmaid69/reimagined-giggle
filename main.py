import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)