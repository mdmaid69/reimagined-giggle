import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)