def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)