def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)