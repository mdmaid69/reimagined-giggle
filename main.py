import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)